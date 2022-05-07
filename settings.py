import pygame
from pygame.locals import *

pygame.init()

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 800,600 # width x height

WINNING_SCORE = 5
SCORE_FONT = pygame.font.SysFont("comicsans", 100)
WINNER_FONT = pygame.font.SysFont("comicsans", 50)

NUM_CAT_FRAME = 49

WHITE = (251,244,229)
PINK = (93.7, 83.9, 83.9)

PADDLE_WIDTH,PADDLE_HEIGHT = 20,100 # width x height 

BALL_RADIUS = 15