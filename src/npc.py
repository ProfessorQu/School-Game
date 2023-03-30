from math import pi, sin
from typing import Tuple, Union
import pygame
from pygame import Vector2
from src.constants import *

from src import utils

class NPC:
    SIZE = 10

    def __init__(self, x, y):
        self.position = Vector2(x, y)
        self.screen_position = utils.convert_to_screen(self.position)
      
    def draw(self, screen: pygame.Surface):
            """Draws the player to the screen

            Args:
                screen (pygame.Surface): the surface to draw on (always screen)
            """
            pygame.draw.circle(
                screen,
                [100, 200, 100],
                self.screen_position,
                self.SIZE
            )
