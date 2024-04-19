#Casey Boyce, Final Project, 0.1
import time, pygame, sys, os

def game_start():
    
    pass

resolution = input('\nResolution:\n    0 for 800 by 600\n    1 for 1920 by 1080 (Default)\n')

# Default values
x = 1920
y = 1080
window_position = (5, 20)

if resolution == '0':
    x = 800
    y = 600

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % window_position

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

if resolution != '0':
    screen.blit(start, (0, 0))
else:
    screen.blit(start_small, (0, 0))

while exiting != True:
    pygame.display.update()

while True:
    keys = pygame.key.get_pressed()
    if screen.blit(start) == True:
        if keys[pygame.K_x]:
            start_passed = True
        else:
            pass
        if start_passed == True:
            if keys[pygame.K_a]:
                pass
            if keys[pygame.K_d]:
                pass
            if keys[pygame.K_w]:
                pass
            if keys[pygame.K_s]:
                pass
    pygame.display.update()

