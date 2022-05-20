from pickle import FALSE
from shutil import move
from tkinter import LEFT


from settings import *

class PlayerComputer:
    def computer_make_paddle_move(ball, left_paddle):
        if ball.y > left_paddle.y - left_paddle.SPEED and left_paddle.y - left_paddle.SPEED >= 0: 
            left_paddle.move(up=True)
        elif ball.y < left_paddle.y + left_paddle.SPEED and left_paddle.y + left_paddle.SPEED + left_paddle.height <= SCREEN_HEIGHT:
            left_paddle.move(up=False)