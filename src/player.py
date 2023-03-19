import pygame
from pygame import Vector2
from src import utils

from src.constants import *
from src.level import Level
from src.room import Room


class Player:
    SIZE = 10
    SPEED = 0.1

    MOVE_ROOM_COOLDOWN = 100

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

        # A timer to keep track of moving through rooms
        self.move_room_timer = self.MOVE_ROOM_COOLDOWN

    def get_inputs(self, current_room: Room):
        """Get the inputs for the player to determine movement
        """
        # If the mouse is pressed and the destination reached
        if pygame.mouse.get_pressed()[0] and self.traveled >= 1:
            # Get a new destination on the tilemap
            tilemap_position = utils.convert_to_tilemap(pygame.mouse.get_pos())
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

            self.screen_position = utils.convert_to_screen(new_position)
            self.traveled += self.SPEED

            # Check x position
            if new_position.x > GRID_WIDTH - 2:
                level.move_room(1, 0)
            elif new_position.x < 1:
                level.move_room(-1, 0)
            # Check y position
            elif new_position.y > GRID_HEIGHT - 2:
                level.move_room(0, -1)
            elif new_position.y < 1:
                level.move_room(0, 1)
        else:
            self.screen_position = utils.convert_to_screen(self.destination)

        # Test for movement time
        if self.move_room_timer <= 0:
            # Check x position
            if self.tilemap_position.x > GRID_WIDTH - 2 and level.move_room(1, 0):
                self.move_room_timer = self.MOVE_ROOM_COOLDOWN
            elif self.tilemap_position.x < 1 and level.move_room(-1, 0):
                self.move_room_timer = self.MOVE_ROOM_COOLDOWN
            # Check y position
            elif self.tilemap_position.y > GRID_HEIGHT - 2 and level.move_room(0, -1):
                self.move_room_timer = self.MOVE_ROOM_COOLDOWN
            elif self.tilemap_position.y < 1 and level.move_room(0, 1):
                self.move_room_timer = self.MOVE_ROOM_COOLDOWN
        
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

    @property
    def tilemap_position(self) -> Vector2:
        """Returns the current tilemap position

        Returns:
            Vector2: the position in the tilemap of the player
        """
        return utils.convert_to_tilemap(self.screen_position)
