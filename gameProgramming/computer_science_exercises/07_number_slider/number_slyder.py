#number slyder, casey boyce, based on a project by Al Sweigart v0.1

import sys, random, pygame
#sys allows systems to access resources

from pygame.locals import *


# contants for game bord
BOARD_WIDTH = 4 #collems
BOARD_HIGHT = 4 #rows
TILE_SIZE = 80 #pixel is the mesure ment
WINDO_WITH = 640 #pixel is the mesure ment
WINDO_HIGHT = 480 #pixel is the mesure ment
FPS = 30 # max value will not snail run quicker
BLANK = None

# COLORS in (R,G,B) format
BLAK = (0,0,0)
WITE = (255,255,255)
BRIGHBLUE = (0,50,255)
DARKTORQOYS = (3,54,73)
GREEN = (0,204,0)

#BOARD DESINE
BG_COLOR = DARKTORQOYS
TILE_COLOR = GREEN
TEXT_COLOR = WITE
BOARDER_COLOR = BRIGHBLUE
BASICFONTSIZE = 20 #pixals

# BUTTON SETUP
BUTTONCOLOR = WITE
BOTTONTEXTCOLOR = BLAK
MESSAGECOLOR = WITE

#establish windo margens
XMARGEN = int((WINDO_WITH - (TILE_SIZE * BOARD_WIDTH + (BOARD_WIDTH - 1)) / 2))
YMARGEN = 