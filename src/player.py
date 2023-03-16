from math import pi, sin
from typing import Tuple, Union
import pygame
from pygame import Vector2

from src.constants import *


class Player:
    SIZE = 10
    SPEED = 0.1

    MOVE_ROOM_TIME = 100

    def __init__(self):
        """Initialize the player
        """
        # The position when you start moving
        self.start_position = Vector2(
            SCREEN_WIDTH / TILE_SIZE / 2,
            SCREEN_HEIGHT / TILE_SIZE / 2
        )
        # The destination clicked on
        self.destination = self.start_position
        # The screen position of the player
        self.screen_position = Vector2(0, 0)

        # A variable to keep track of the amount traveled from start_position to destination
        self.traveled = 0

        self.move_room_timer = self.MOVE_ROOM_TIME

    def get_inputs(self, current_room):
        """Get the inputs for the player to determine movement
        """
        # If the mouse is pressed and the destination reached
        if pygame.mouse.get_pressed()[0] and self.traveled >= 1:
            # Get a new destination on the tilemap
            tilemap_position = self.convert_to_tilemap(pygame.mouse.get_pos())
            if tilemap_position in current_room.walls:
                return

            self.destination = tilemap_position
            self.start_position = self.tilemap_position
            self.traveled = 0

    def update(self, level: Level):
        """Update the position of the player
        """
        if self.move_room_timer > 0:
            self.move_room_timer -= 1

        if self.traveled < 1:
            new_position = self.start_position.lerp(
                self.destination,
                self.traveled
            )

            self.screen_position = self.convert_to_screen(new_position)
            self.traveled += self.SPEED
        else:
            self.screen_position = self.convert_to_screen(self.destination)

        # Test for movement time
        if self.move_room_timer <= 0:
            # Check x position
            if self.tilemap_position.x > GRID_WIDTH - 2 and level.move_room(1, 0):
                self.move_room_timer = self.MOVE_ROOM_TIME
            elif self.tilemap_position.x < 1 and level.move_room(-1, 0):
                self.move_room_timer = self.MOVE_ROOM_TIME
            # Check y position
            elif self.tilemap_position.y > GRID_HEIGHT - 2 and level.move_room(0, -1):
                self.move_room_timer = self.MOVE_ROOM_TIME
            elif self.tilemap_position.y < 1 and level.move_room(0, 1):
                self.move_room_timer = self.MOVE_ROOM_TIME
        
    def draw(self, screen: pygame.Surface):
        """Draws the player to the screen

        Args:
            screen (pygame.Surface): the surface to draw on (always screen)
        """
        pygame.draw.circle(
            screen,
            [200, 10, 30],
            self.screen_position,
            self.SIZE
        )

    def convert_to_tilemap(self, vec: Union[Vector2, Tuple[int, int]]) -> Vector2:
        """Convert the screen coordinates to tilemap coordinates

        Args:
            vec (Union[Vector2, Tuple[int, int]]): the screen coordinates

        Returns:
            Vector2: the tilemap coordinates
        """
        return Vector2(
            vec[0] // TILE_SIZE,
            vec[1] // TILE_SIZE
        )

    def convert_to_screen(self, vec: Union[Vector2, Tuple[int, int]]) -> Vector2:
        """Convert the tilemap coordinates to screen coordinates

        Args:
            vec (Union[Vector2, Tuple[int, int]]): the tilemap coordinates

        Returns:
            Vector2: the screen coordinates
        """
        new = pygame.math.Vector2(vec[0], vec[1])
        new *= TILE_SIZE
        new.x += TILE_SIZE / 2
        new.y += TILE_SIZE / 2

        return pygame.Vector2(new)

    @property
    def tilemap_position(self) -> Vector2:
        """Returns the current tilemap position

        Returns:
            Vector2: the position in the tilemap of the player
        """
        return self.convert_to_tilemap(self.screen_position)
