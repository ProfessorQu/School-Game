import pygame
from pygame import Vector2

from src.utils.constants import *
from src.player import Player
from src.npc import NPC
from src.level import Level
from src.room import Room

from src.utils.dialogue import Dialogue, Line


def main():
    pygame.init()

    # Create a screen, a clock and a player
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    player = Player()

    pygame.mixer.init()
    # Load and play the music
    pygame.mixer.music.load("assets/sounds/backgroundmusic.ogg")
    # Music loopen
    pygame.mixer.music.play(-1)
    # Volume of the song
    pygame.mixer.music.set_volume(0.1)

    pygame.display.set_caption("School game")

    running = True

    level = Level(
        [
            Room(0, 0, [Vector2(x, y) for x in range(5) for y in range(3)],
                [
                    NPC(5, 5, "Korné",
                        Dialogue(
                            "heroine",
                            "knijptang",
                            Line("Geef die heroine maar, dan krijg jij de sleutel\nvan het informatica lokaal.", "korné_wel"),
                            Line("N-n-n-n nee! Je hebt niks.\nGeef me heroine! Geef, geef, geef!", "korné_niet")
                        )
                    )
                ]
            ),
            Room(1, 0, [Vector2(x, y) for x in range(10) for y in range(5)],
                [
                    NPC(7, 10, "Joost",
                        Dialogue(
                            "knijptang",
                            "sleutel",
                            Line("Nee! Hoe durf je?!\nStelen van je eigen informatica docent?!", "joost_wel"),
                            Line("Hallo, wat is er? Sleutel? Nee die ligt hier niet.", "joost_niet")
                        )
                    )
                ]
            ),
            Room(2, 0, [Vector2(x, y) for x in range(15) for y in range(5)], []),
            Room(1, 1, [Vector2(x, y) for x in range(15) for y in range(5)], [])
        ]
    )

    while running:
        # Test for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                player.update(level, event.key)

        SCREEN.fill((100, 100, 200))

        # Draw things
        level.draw_background(SCREEN)
        player.draw(SCREEN)
        level.draw_text_box(SCREEN)

        # Update the display
        pygame.display.flip()

        # Run at 60 FPS
        CLOCK.tick(60)
    
    pygame.quit()


if __name__ == '__main__':
    main()
