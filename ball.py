import pygame
from pygame.locals import *

class Ball:
    MAX_SPEED = 5

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.x_speed = self.MAX_SPEED
        self.y_speed = 0

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed