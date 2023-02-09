import pygame
from pygame import Vector2

from src.constants import *


class Player:
    SIZE = 10
    SPEED = 1

    def __init__(self):
        self.destination = Vector2(0, 0)
        self.position = Vector2(0, 0)

    def get_inputs(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            position = Vector2(
                mouse_pos[0] // TILE_SIZE,
                mouse_pos[1] // TILE_SIZE
            )

            if position == WALL:
                return

            position *= TILE_SIZE
            position.x += TILE_SIZE / 2
            position.y += TILE_SIZE / 2

            self.destination = position

    def update(self):
        self.position = self.position.lerp(self.destination, 0.1)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, [100, 10, 30], self.position, self.SIZE)
