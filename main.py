import pygame

from assets import MultiLineLabel, Label


def home_screen():
    title = Label("TETRIS", 50, white, (width/2, height/5))
    cont = Label("(Press any key to play)", 15, white, (width / 2, height / 5 + 30))
    bg = pygame.image.load("tetris_bg.png")

    while 1:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                pass
                game()

        screen.fill(black)
        screen.blit(bg, (0, 0))
        title.draw(screen)
        cont.draw(screen)
        pygame.display.update()


def game():
    bg_rects = []
    for i in range(rows):
        rect = pygame.Rect(game_width / 10, height, ((i * game_width / 10) - 25, 300), white)
        bg_rects.append(rect)

    for rect in bg_rects:
        pygame.draw.rect(screen, white, )

    while 1:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            screen.fill(black)
            pygame.draw.line(screen, white, (300, 0), (300, 600))
            pygame.display.update()


if __name__ == '__main__':
    size = width, height = 500, 600
    game_width = 300
    rows = 10
    columns = 20
    square = 30

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tetris')

    home_screen()

