#Casey Boyce, Final Project, 0.1
import time, pygame, sys

resilution = 0 # 0 for low. 1 for high

if resilution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

screen = pygame.display.set_mode((x,y))

difficulty = input("Please chose a Difficulty Easy or Hard.\n").capitalize

if difficulty == "EASY":
    pygame.display.set_caption('Jumpin To Da Top -- Grandmama Mode')
else:
    pygame.display.set_caption("Why Did You Pick This Mode")