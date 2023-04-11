from typing import Union
import pygame
from pygame import Vector2
from src.utils.constants import *

from src.utils import utils
from src.utils.dialogue import Line
from src.utils.dialogue import Dialogue

class NPC:
    SIZE = 10


    def __init__(
            self, x: int, y: int, name: str,
            has_item: str, get_item: str, has_text: str, get_text: str,
            should_destroy: bool = False
        ):
        """Init NPC

        Args:
            x (int): x pos
            y (int): y pos
            name (str): name
            has_item (str): required item
            get_item (str): what item to get
            has_text (str): the text for when you have required item
            get_text (str): the text for when you don't have required item
        """
        self.name = name

        # Set position
        self.position = Vector2(x, y)
        self.screen_position = utils.convert_to_screen(self.position) - Vector2(TILE_SIZE) / 2

        # Load image
        image = pygame.image.load(f"assets/images/npcs/{self.name.lower()}.png")
        self.image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)).convert_alpha()

        if get_item is not None:
            has_text += f"\n{{{get_item.capitalize()} verkregen}}"

        self.dialogue = Dialogue(
            has_item,
            get_item,
            Line(has_text, f"{self.name}_wel"),
            Line(get_text, f"{self.name}_niet"),
        )

        self.should_destroy = should_destroy

        self.current_line = None


    def get_line(self, player) -> str:
        """Get the current line of the npc

        Args:
            player (Player): the player

        Returns:
            str: the line
        """
        has_item, self.current_line = self.dialogue.get_current_line(player.items)

        if has_item:
            player.items.remove(self.dialogue.has_item)
            if self.dialogue.get_item:
                player.items.append(self.dialogue.get_item)

        return self.current_line.text


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
