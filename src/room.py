import pygame

from src.constants import *

class Room:
    def __init__(self, x, y, walls, npcs) -> None:
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
    
    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(
                screen,
                (100, 100, 100),
                [
                    wall.x * TILE_SIZE,
                    wall.y * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                ]
            )
