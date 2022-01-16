import pygame


def home_screen():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        screen.blit(text, title)

        pygame.display.update()


def game():
    while 1:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)

        pygame.display.update()


if __name__ == '__main__':

    size = width, height = 300, 500
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    pygame.init()

    screen = pygame.display.set_mode(size)

    home_screen()

