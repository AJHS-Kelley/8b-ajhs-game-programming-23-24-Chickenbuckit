#Casey Boyce, Final Project, 0.1
import time, pygame, sys, os 

resilution = input('\nresilution:\n    0 for 800 by 600\n    1 for 1920 by 1080 (Defalt)\n') # 0 for low. 1 for high
a = 20
z = 5
if resilution == '0':
    x = 800
    y = 600
else:
    x = 1920
    y = 1080
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (z,a)

screen = pygame.display.set_mode((x,y))
start_time = pygame.time.get_ticks()
difficulty = input("\n\nPlease chose a Difficulty Easy or Hard.\nDefalt is Easy\n\n").lower()

if difficulty == "hard":
    pygame.display.set_caption("Leaping Ruler -- Dont Fall Now ")
else:
    pygame.display.set_caption("Leaping Ruler -- Baby Mode ")

start = pygame.image.load('gameProgramming/IMG/bg water/Start.png')
start_small = pygame.image.load('gameProgramming/IMG/bg water/Start_smallrez.png')

exiting = False

if resilution != '0':
    screen.blit(start, (0, 0))
else:
    screen.blit(start_small, (0, 0))

while exiting != True:
    pygame.display.update()
