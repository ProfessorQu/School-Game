import pygame
from pygame import Vector2

from src.constants import *
from src.player import Player
from src.npc import NPC
from src.level import Level
from src.room import Room


def main():
    # Create a screen, a clock and a player
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    player = Player()

    pygame.display.set_caption("School game")

    running = True

    level = Level(
        [
            Room(0, 0, [
                Vector2(x, y) for x in range(5) for y in range(3)
            ], [NPC(5, 5)]),
            Room(1, 0, [
                Vector2(x, y) for x in range(10) for y in range(5)
            ], []),
            Room(2, 0, [
                Vector2(x, y) for x in range(15) for y in range(5)
            ], []),
            Room(1, 1, [
                Vector2(x, y) for x in range(15) for y in range(5)
            ], [])
        ]
    )

    while running:
        # Test for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                player.update(level, event.key)

        # player.get_inputs(level.current_room)
        # player.update(level)

        # Fill the screen
        SCREEN.fill((100, 100, 200))

        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            pygame.draw.line(
                SCREEN,
                (200, 200, 200),
                [x, 0],
                [x, SCREEN_WIDTH]
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

        level.current_room.draw(SCREEN)

        # Update the display
        pygame.display.flip()

        # Run at 60 FPS
        CLOCK.tick(60)


if __name__ == '__main__':
    main()
