from typing import List, Tuple
import pygame


class Line:
    def __init__(self, line: str, voiceline_file: str):
        """Initialize the line

        Args:
            line (str): the line in the textbox
            voiceline_file (str): the name of the voiceline
        """
        self.line = line
        if voiceline_file:
            self.voiceline = pygame.mixer.Sound(f"assets/sounds/npcs/{voiceline_file}.ogg")
        else:
            self.voiceline = None
    
    def play_voiceline(self):
        """Play the voiceline
        """
        if self.voiceline:
            self.voiceline.play()
    
    def get_line(self) -> str:
        """Get the line

        Returns:
            str: the line
        """
        return self.line


class Dialogue:
    def __init__(self, item: str, get_item: str, has_line: Line, other_line: Line):
        """Initialize the dialogue

        Args:
            item (str): the required item
            has_line (Line): the line if you have it
            other_line (Line): the line if you don't
        """
        self.has_item = item
        self.get_item = get_item
        self.has_line = has_line
        self.other_line = other_line
    
    def get_line(self, items: List[str]) -> Tuple[bool, Line]:
        """Return the current line

        Args:
            items (List[str]): the list of items

        Returns:
            bool, Line: have the required item, the current line
        """
        return self.has_item in items, self.has_line if self.has_item in items else self.other_line
