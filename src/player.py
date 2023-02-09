import pygame
from pygame import Vector2


class Player:
    SIZE = 10
    SPEED = 1

    def __init__(self):
        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    def get_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velocity.x -= self.SPEED
        if keys[pygame.K_RIGHT]:
            self.velocity.x += self.SPEED

        if keys[pygame.K_UP]:
            self.velocity.y -= self.SPEED
        if keys[pygame.K_DOWN]:
            self.velocity.y += self.SPEED

    def update(self):
        self.position += self.velocity

        self.velocity *= 0.01

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, [100, 10, 30], self.position, self.SIZE)
