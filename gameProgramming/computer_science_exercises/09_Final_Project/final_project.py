#Casey Boyce, Final Project, 0.1
import time, pygame, sys, os

def bg_animation():
    while True:
        screen.blit('gameProgramming/IMG/bg water/pixil-frame-0.png')
        pygame.display.update()
        time.sleep(3)
        screen.blit('gameProgramming/IMG/bg water/pixil-frame-1.png')
        pygame.display.update()
        time.sleep(3)
        screen.blit('gameProgramming/IMG/bg water/pixil-frame-2.png')
        pygame.display.update()
        time.sleep(3)

def ground():
    screen.fill('gameProgramming/IMG/bg water/groundsand.png')

def game_start():
    bg_animation()
    ground()

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

if resolution != '0':
    screen.blit(start, (0, 0))
else:
    screen.blit(start_small, (0, 0))

pygame.init()

start_passed = False

def game_start():
    # Function to start the game
    pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if start_passed:
        if keys[pygame.K_a]:
            pass
        if keys[pygame.K_d]:
            pass
        if keys[pygame.K_w]:
            pass
        if keys[pygame.K_s]:
            pass
    else:
        if keys[pygame.K_x]:
            start_passed = True
            game_start()

    pygame.display.update()