import pygame
from random import randint

pygame.init()
size = 400, 200
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
timer = 0
running = True
font = pygame.font.Font(None, 50)
font_2 = pygame.font.Font(None, 20)
text = font.render("Здесь будет игра", 1, (0, 200, 200))
text_2 = font_2.render("Когда-нибудь", 1, (0, 100, 100))
text_x = 200 - text.get_width() // 2
text_y = 80 - text.get_height() // 2
text_2_x = 200 - text_2.get_width() // 2
text_2_y = 150 - text_2.get_height() // 2


screen.blit(text, (text_x, text_y))
screen.blit(text_2, (text_2_x, text_2_y))
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    timer += clock.tick()
    if timer >= 1000:
        timer = 0
        color = (randint(110, 256), randint(110, 256), randint(110, 256))
        color_2 = (color[0] - 100, color[1] - 100, color[2] - 100)
        text = font.render("Здесь будет игра", 1, color)
        text_2 = font_2.render("Когда-нибудь", 1, color_2)
        screen.blit(text, (text_x, text_y))
        screen.blit(text_2, (text_2_x, text_2_y))
        pygame.display.flip()
