# ultimate intro into pygame casey boyce v0.2
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font("comicsansms", 50)

sky_box = pygame.image.load('img\download.jpg')
grond_surface = pygame.image.load('img\gross.png')
text_surface = test_font.render("Casey's game", False, 'black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(grond_surface, (0, 0))
    screen.blit(sky_box, (0, 300))
    screen.blit(text_surface, (300, 50))
    pygame.display.update()
    clock.tick(60)