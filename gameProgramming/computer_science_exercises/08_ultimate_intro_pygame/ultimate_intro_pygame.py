# ultimate intro into pygame casey boyce v0.5
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
text_surface = test_font.render("Casey's game", False, 'black')

snail_enimy = pygame.image.load('img\Snail.png').convert_alpha()
snail_rect = snail_enimy.get_rect(midbottem = (800,300))


player_surf = pygame.image.load('img/grandma.png').convert_alpha()
player_rect = player_surf.get_rect(midbottem = (80,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(grond_surface, (0, 300))
    screen.blit(sky_box, (0, 0))
    screen.blit(text_surface, (300, 50))
    snail_rect.x -= 6
    if snail_rect.right < 0 : snail_rect.left = 800
    screen.blit(snail_enimy, snail_rect)
    screen.blit(player_surf, player_rect)
    if player_rect.colliderect(snail_rect):
        exit()
    pygame.display.update()
    clock.tick(60)