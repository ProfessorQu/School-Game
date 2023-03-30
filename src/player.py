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
        # The tilemap position of the player
        self.position = Vector2(GRID_WIDTH / 2, GRID_HEIGHT / 2)

        # A timer to keep track of moving through rooms
        self.move_room_timer = self.MOVE_ROOM_COOLDOWN

    def update(self, level: Level, key):
        """Get the inputs for the player to determine movement
        """
        move = pygame.Vector2(0, 0)
        # Set the move according to the key pressed
        if key == pygame.K_w:
            move.y = -1
        elif key == pygame.K_s:
            move.y = 1
        elif key == pygame.K_d:
            move.x = 1
        elif key == pygame.K_a:
            move.x = -1

        new_position = self.position + move

        # Check x position
        if new_position.x > GRID_WIDTH - 2:
            if level.move_room(1, 0):
                self.position.x = 1
                return
        elif new_position.x < 1:
            if level.move_room(-1, 0):
                self.position.x = GRID_WIDTH - 2
                return
        # Check y position
        elif new_position.y > GRID_HEIGHT - 2:
            if level.move_room(0, -1):
                self.position.y = 1
                return
        elif new_position.y < 1:
            if level.move_room(0, 1):
                self.position.y = GRID_HEIGHT - 2
                return

        if new_position in level.current_room.walls:
            return

        self.position = new_position

    def draw(self, screen: pygame.Surface):
        """Draws the player to the screen

        Args:
            screen (pygame.Surface): the surface to draw on (always screen)
        """
        pygame.draw.circle(
            screen,
            [200, 10, 30],
            utils.convert_to_screen(self.position),
            self.SIZE
        )
