from typing import Union
import pygame
from pygame import Vector2
from src.utils.constants import *

from src.utils import utils
from src.utils.dialogue import Line
from src.utils.dialogue import Dialogue

class NPC:
    SIZE = 10

    def __init__(self, x: int, y: int, name: str, dialogue: Dialogue):
        """Init NPC

        Args:
            x (int): the x position
            y (int): the y position
            name (str): the name of the NPC
            dialogue (str): the dialogue of the NPC
        """
        self.name = name

        # Set position
        self.position = Vector2(x, y)
        self.screen_position = utils.convert_to_screen(self.position) - Vector2(TILE_SIZE) / 2

        # Load image
        image = pygame.image.load(f"assets/images/npcs/{self.name.lower()}.png")
        self.image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)).convert_alpha()

        self.dialogue = dialogue

        self.current_line = None

    def get_line(self, player) -> str:
        has_item, self.current_line = self.dialogue.get_line(player.items)

        if has_item:
            player.items.remove(self.dialogue.item)

        return self.current_line.line

    def play_voiceline(self):
        """Play the voiceline
        """
        self.current_line.play_voiceline()
      
    def draw(self, screen: pygame.Surface):
        """Draws the player to the screen

        Args:
            screen (pygame.Surface): the surface to draw on (always screen)
        """
        screen.blit(self.image, self.screen_position)
