import pygame
from pygame import Vector2

from typing import List, Union

from src.utils.constants import *
from src.npc import NPC

class Room:
    def __init__(self, x: int, y: int,
                 left_entry: bool, top_entry: bool, right_entry: bool, bottom_entry: bool,
                 walls: List[Vector2], npcs: List[NPC]):
        """Initialize Room

        Args:
            x (int): the x position of the room in the level
            y (int): the y position of the room in the level
            walls (List[Vector2]): the list of walls in the level
        """
        self.x = x
        self.y = y

        self.walls = walls
        self.npcs = npcs

        self.walls += [Vector2(0, y) for y in range(GRID_HEIGHT) if left_entry or y not in LEFT_RIGHT_ENTRIES]
        self.walls += [Vector2(GRID_WIDTH - 1, y) for y in range(GRID_HEIGHT) if right_entry or y not in LEFT_RIGHT_ENTRIES]
        self.walls += [Vector2(x, 0) for x in range(GRID_WIDTH) if top_entry or x not in TOP_BOTTOM_ENTRIES]
        self.walls += [Vector2(x, GRID_HEIGHT - 1) for x in range(GRID_WIDTH) if bottom_entry or x not in TOP_BOTTOM_ENTRIES]

        wall_image = pygame.image.load("assets/images/wall.png")
        self.wall_image = pygame.transform.scale(wall_image, (TILE_SIZE, TILE_SIZE))
    
    def get_npc(self, pos: Vector2) -> Union[NPC, None]:
        """Return an NPC if there is one at pos

        Args:
            npc (Vector2): the position of the NPC

        Returns:
            Union[NPC, None]: returns None if there is no NPC, otherwise returns the npc
        """
        return next(
            (npc for npc in self.npcs if npc.position == pos), None
        )
    
    def draw(self, screen: pygame.Surface):
        """Draw this room

        Args:
            screen (pygame.Surface): the screen
        """
        for wall in self.walls:
            screen.blit(
                self.wall_image, pygame.Rect(
                    wall.x * TILE_SIZE,
                    wall.y * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                )
            )
        
        for npc in self.npcs:
            npc.draw(screen)
