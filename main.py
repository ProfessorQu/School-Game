import pygame


def main():
    screen = pygame.display.set_mode((300, 300))

    pygame.display.set_caption("School game")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((100, 100, 200))

        pygame.display.flip()


if __name__ == '__main__':
    main()
