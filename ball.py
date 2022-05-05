import pygame
from pygame.locals import *

from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Ball:
    MAX_SPEED = 7

    def __init__(self, x, y, radius):
        self.x = self.ORIGINAL_X = x
        self.y = self.ORIGINAL_Y = y
        self.radius = radius

        self.x_speed = self.MAX_SPEED
        self.y_speed = 0

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def reset(self):
        self.x = self.ORIGINAL_X
        self.y = self.ORIGINAL_Y
        self.y_speed = 0
        self.x_speed *= -1