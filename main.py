import pygame

from src.utils.constants import *
from src.player import Player

from src.utils.init_level import init_level


def main():
    pygame.init()

    # Create a screen, a clock and a player
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    player = Player()

    pygame.mixer.init()
    # Load and play the music
    pygame.mixer.music.load("assets/sounds/backgroundmusic.ogg")
    # Loop music
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    pygame.display.set_caption("School game")

    running = True

    level = init_level()

    win_image = pygame.image.load("assets/images/winscreen.png")

    while running:
        # Test for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                player.update(level, event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN and player.won():
                if pygame.mouse.get_pressed()[0]:
                    running = False

        SCREEN.fill((100, 100, 200))

        if player.won():
            SCREEN.blit(win_image, (0, 0))
        else:
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
