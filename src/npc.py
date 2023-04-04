import pygame
from pygame import Vector2
from src.constants import *

from src import utils

class NPC:
    SIZE = 10

    def __init__(self, x: int, y: int, name: str, dialogue: str):
        """Init NPC

        Args:
            x (int): the x position
            y (int): the y position
            name (str): the name of the NPC
            dialogue (str): the dialogue of the NPC
        """
        self.name = name

        self.position = Vector2(x, y)
        self.screen_position = utils.convert_to_screen(self.position) - Vector2(TILE_SIZE) / 2

        image = pygame.image.load(f"assets/{self.name.lower()}.png")
        self.image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)).convert_alpha()

        self.dialogue = dialogue
      
    def draw(self, screen: pygame.Surface):
        """Draws the player to the screen

        Args:
            screen (pygame.Surface): the surface to draw on (always screen)
        """
        screen.blit(self.image, self.screen_position)
        # pygame.draw.circle(
        #     screen,
        #     [100, 200, 100],
        #     self.screen_position,
        #     self.SIZE
        # )
