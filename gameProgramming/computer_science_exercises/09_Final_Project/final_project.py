#Casey Boyce, Final Project, 0.1
import time, pygame, sys, os
#loading images (if it does anything)
darkness = pygame.image.load('gameProgramming/IMG/bg water/Black filler.png')
sands = pygame.image.load('gameProgramming/IMG/bg water/groundsandSmall.png')
sand = pygame.image.load('gameProgramming/IMG/bg water/groundsand.png')
frame0 = pygame.image.load('gameProgramming/IMG/bg water/pixil-frame-0.png')
frame0s = pygame.image.load('gameProgramming/IMG/bg water/pixil-frame-0Small.png')
frame1 = pygame.image.load('gameProgramming/IMG/bg water/pixil-frame-1.png')
frame1s = pygame.image.load('gameProgramming/IMG/bg water/pixil-frame-1Small.png')
frame2 = pygame.image.load('gameProgramming/IMG/bg water/pixil-frame-2.png')
frame2s = pygame.image.load('gameProgramming/IMG/bg water/pixil-frame-2Small.png')
starts = pygame.image.load('gameProgramming/IMG/bg water/Start_smallrez.png')
start = pygame.image.load('gameProgramming/IMG/bg water/Start.png')

def bg_animation():
    while True:
        if resolution == '0':
            screen.blit(darkness, (0, 0))
            screen.blit(frame0s, (0, 0))
            pygame.display.update()
            time.sleep(3)
            screen.blit(frame1s, (0, 0))
            pygame.display.update()
            time.sleep(3)
            screen.blit(frame2s, (0, 0))
            pygame.display.update()
            time.sleep(3)
        else:
            screen.blit(darkness, (0, 0))
            screen.blit(frame0, (450, 50))
            pygame.display.update()
            time.sleep(3)
            screen.blit(frame1, (450, 50))
            pygame.display.update()
            time.sleep(3)
            screen.blit(frame2, (450, 50))
            pygame.display.update()
            time.sleep(3)
        pygame.display.update()

#class Platform(pygame.sprite.Sprite): #NOT DONE YET
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('gameProgramming/IMG/Fsh1.png', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

def ground():
    if resolution == '0':
        while True:
            pygame.display.update()
            screen.blit(sands, (0, 0))
    else:
        while True:
            pygame.display.update()
            screen.blit(sand, (0, 0))        

def game_start():
    bg_animation()

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

if resolution != '0':
    screen.blit(start, (0, 0))
else:
    screen.blit(starts, (0, 0))

pygame.init()

start_passed = False

# movement
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
        if keys[pygame.K_SPACE]:
            pass
    else:
        if keys[pygame.K_x]:
            start_passed = True
            game_start()

    pygame.display.update()