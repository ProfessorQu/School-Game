from math import pi, sin
from typing import Tuple, Union
import pygame
from pygame import Vector2

from src.constants import *

def convert_to_tilemap(vec: Union[Vector2, Tuple[int, int]]) -> Vector2:
    """Convert the screen coordinates to tilemap coordinates

    Args:
        vec (Union[Vector2, Tuple[int, int]]): the screen coordinates

    Returns:
        Vector2: the tilemap coordinates
    """
    return Vector2(
        vec[0] // TILE_SIZE,
        vec[1] // TILE_SIZE
    )

def convert_to_screen(vec: Union[Vector2, Tuple[int, int]]) -> Vector2:
    """Convert the tilemap coordinates to screen coordinates

    Args:
        vec (Union[Vector2, Tuple[int, int]]): the tilemap coordinates

    Returns:
        Vector2: the screen coordinates
    """
    new = pygame.math.Vector2(vec[0], vec[1])
    new *= TILE_SIZE
    new.x += TILE_SIZE / 2
    new.y += TILE_SIZE / 2

    return pygame.Vector2(new)