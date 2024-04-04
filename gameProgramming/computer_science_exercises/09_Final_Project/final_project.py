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
start_time = pygame.time.get_ticks()
difficulty = input("\n\nPlease chose a Difficulty Easy or Hard.\n\n\nDefalt is Easy  ").lower

if difficulty == "hard":
    pygame.display.set_caption("Leaping Ruler -- Dont Fall Now ")
else:
    pygame.display.set_caption("Leaping Ruler -- Baby Mode ")

time.sleep(5)
