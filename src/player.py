import pygame
from pygame import Vector2


class Player:
    size = 10

    def __init__(self) -> None:
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def update(self) -> None:
        self.position += self.velocity

        self.velocity *= 0.01

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, [100, 10, 30], self.position, self.size)
