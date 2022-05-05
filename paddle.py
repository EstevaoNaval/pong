import pygame
from pygame.locals import *

class Paddle:
    SPEED = 6

    def __init__(self, x, y, width, height):
        self.x = self.ORIGINAL_X = x
        self.y = self.ORIGINAL_Y = y
        self.height = height
        self.width = width

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up: self.y -= self.SPEED
        else: self.y += self.SPEED
    
    def reset(self):
        self.x = self.ORIGINAL_X
        self.y = self.ORIGINAL_Y