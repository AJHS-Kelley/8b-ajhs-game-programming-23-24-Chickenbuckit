# ultimate intro into pygame casey boyce v0.1
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

grond_surface = pygame.image.load('img\gross.jpg')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(grond_surface, (0, 0))
    pygame.display.update()
    clock.tick(60)