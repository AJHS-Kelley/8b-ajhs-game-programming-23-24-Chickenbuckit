# ultimate intro into pygame casey boyce v0.3
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
all_fonts = pygame.font.get_fonts()
test_font = pygame.font.SysFont("comicsansms", 50)

sky_box = pygame.image.load('img\download.jpg').convert()
grond_surface = pygame.image.load('img\gross.png').convert()
text_surface = test_font.render("Casey's game", False, 'black').convert()

snail_enimy = pygame.image.load('img\Snail.png')
snail_x_pos = 800
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(grond_surface, (0, 300))
    screen.blit(sky_box, (0, 0))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 6
    if snail_x_pos < -100 : snail_x_pos = 800
    screen.blit(snail_enimy,(snail_x_pos, 250))
    pygame.display.update()
    clock.tick(60)