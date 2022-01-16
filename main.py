import pygame

size = width, height = 320, 240
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('2048')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('text', True, black, white)

textRect = text.get_rect()
textRect.center = (width // 2, height // 2)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    screen.blit(text, textRect)

    pygame.display.update()

