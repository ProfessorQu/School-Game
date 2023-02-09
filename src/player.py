from typing import Tuple, Union
import pygame
from pygame import Vector2

from src.constants import *


class Player:
    SIZE = 10
    SPEED = 0.1

    def __init__(self):
        self.start_position = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.screen_position = Vector2(0, 0)

        self.traveled = 0

    def get_inputs(self):
        if pygame.mouse.get_pressed()[0] and self.traveled >= 1:
            tilemap_position = self.convert_to_tilemap(
                pygame.mouse.get_pos())
            if tilemap_position == WALL:
                return

            self.destination = self.convert_to_screen(tilemap_position)
            self.start_position = self.screen_position
            self.traveled = 0

    def update(self):
        if self.traveled < 1:
            self.screen_position = self.start_position.lerp(
                self.destination, self.traveled)

            self.traveled += self.SPEED
        else:
            self.screen_position = self.destination

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            [100, 10, 30],
            self.screen_position,
            self.SIZE
        )

    def convert_to_tilemap(self, vec: Union[Vector2, Tuple[int, int]]) -> Vector2:
        return Vector2(
            vec[0] // TILE_SIZE,
            vec[1] // TILE_SIZE
        )

    def convert_to_screen(self, vec: Vector2) -> Vector2:
        vec *= TILE_SIZE
        vec.x += TILE_SIZE / 2
        vec.y += TILE_SIZE / 2

        return vec
