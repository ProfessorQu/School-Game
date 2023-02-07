import pygame
from pygame import Vector2

from src.player import Player

SPEED = 1e-2


def main():
    screen = pygame.display.set_mode((512, 512))
    player = Player()

    pygame.display.set_caption("School game")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_velocity(player)
        player.update()

        screen.fill((100, 100, 200))
        player.draw(screen)
        pygame.display.flip()


def update_velocity(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.velocity.x -= SPEED
    if keys[pygame.K_RIGHT]:
        player.velocity.x += SPEED

    if keys[pygame.K_UP]:
        player.velocity.y -= SPEED
    if keys[pygame.K_DOWN]:
        player.velocity.y += SPEED


if __name__ == '__main__':
    main()
