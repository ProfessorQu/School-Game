import pygame
from pygame import Vector2

from src.constants import *
from src.player import Player


def main():
    # Create a screen, a clock and a player
    SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    CLOCK = pygame.time.Clock()
    player = Player()

    pygame.display.set_caption("School game")

    running = True

    while running:
        # Test for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.get_inputs()
        player.update()

        # Fill the screen
        SCREEN.fill((100, 100, 200))

        for x in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(
                SCREEN,
                (200, 200, 200),
                [x, 0],
                [x, SCREEN_HEIGHT]
            )

        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(
                SCREEN,
                (200, 200, 200),
                [0, y],
                [SCREEN_WIDTH, y]
            )

        # Draw the player
        player.draw(SCREEN)

        for wall in WALLS:
            pygame.draw.rect(
                SCREEN,
                (100, 100, 100),
                [
                    wall.x * TILE_SIZE,
                    wall.y * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE
                ]
            )

        # Update the display
        pygame.display.flip()

        # Run at 60 FPS
        CLOCK.tick(60)


if __name__ == '__main__':
    main()
