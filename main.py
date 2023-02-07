import pygame
from pygame import Vector2

from src.player import Player


def main():
    # Create a screen, a clock and a player
    SCREEN = pygame.display.set_mode((512, 512))
    CLOCK = pygame.time.Clock()
    player = Player()

    pygame.display.set_caption("School game")

    running = True

    while running:
        # Test for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update_velocity()
        player.update()

        # Fill the screen
        SCREEN.fill((100, 100, 200))

        # Draw the player
        player.draw(SCREEN)

        # Update the display
        pygame.display.flip()

        # Run at 60 FPS
        CLOCK.tick(60)


if __name__ == '__main__':
    main()
