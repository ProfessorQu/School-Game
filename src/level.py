import itertools
from typing import List

import pygame

from src.room import Room
from src.constants import *

class Level:
    def __init__(self, rooms: List[Room]) -> None:
        """Initialize level

        Args:
            rooms (List[Room]): a list of rooms in this level
        """
        self.rooms = rooms

        self.current_room_x = 0
        self.current_room_y = 0

        self.current_npc = None

        self.font = pygame.font.SysFont("", 40)

        floor_image = pygame.image.load("assets/images/floor.png").convert()
        self.floor_image = pygame.transform.scale(floor_image, (TILE_SIZE, TILE_SIZE))
    
    def draw(self, screen: pygame.Surface):
        """Draw the level

        Args:
            screen (pygame.Surface): the screen
        """
        for x, y in itertools.product(range(GRID_WIDTH), range(GRID_HEIGHT)):
            screen.blit(self.floor_image, (x * TILE_SIZE, y * TILE_SIZE))

        # Draw the current room
        self.current_room.draw(screen)

        # Draw dialogue from npcs
        if self.current_npc:
            self.draw_text_box(screen)

    def draw_text_box(self, screen):
        # Draw the name
        text_surface = self.font.render(self.current_npc.name, True, (0, 0, 0))
        screen.blit(text_surface, (0, SCREEN_HEIGHT / 2 - TEXT_BOX_BORDER_THICKNESS * 3, SCREEN_WIDTH, 100))

        # Draw the text box
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            pygame.Rect(
                0,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH,
                SCREEN_HEIGHT / 2
            )
        )

        pygame.draw.rect(
            screen,
            (240, 240, 240),
            pygame.Rect(
                TEXT_BOX_BORDER_THICKNESS,
                SCREEN_HEIGHT / 2 + TEXT_BOX_BORDER_THICKNESS,
                SCREEN_WIDTH - TEXT_BOX_BORDER_THICKNESS * 2,
                SCREEN_HEIGHT / 2 - TEXT_BOX_BORDER_THICKNESS * 2
            )
        )

        # Draw the text
        text_surface = self.font.render(self.current_npc.dialogue, True, (0, 0, 0))
        screen.blit(text_surface, (2 * TEXT_BOX_BORDER_THICKNESS, SCREEN_HEIGHT / 2 + 2 * TEXT_BOX_BORDER_THICKNESS))

    def move_room(self, x: int, y: int) -> bool:
        """Move the current room with an offset of x and y

        Args:
            x (int): the distance to move the room in the x-axis
            y (int): the distance to move the room in the y-axis
        """
        new_room_x = self.current_room_x + x
        new_room_y = self.current_room_y + y

        for room in self.rooms:
            if room.x == new_room_x and room.y == new_room_y:
                self.current_room_x = new_room_x
                self.current_room_y = new_room_y

                return True

        return False

    @property
    def current_room(self) -> Room:
        """Get the current room

        Raises:
            ValueError: If there is no room with the current index

        Returns:
            Room: the current room
        """
        for room in self.rooms:
            if room.x == self.current_room_x and room.y == self.current_room_y:
                return room

        raise ValueError(
            f"X: {self.current_room_x}, Y: {self.current_room_y} are not rooms")
