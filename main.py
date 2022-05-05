from math import ceil
import pygame, sys
from pygame.locals import *
from settings import *
from paddle import Paddle
from ball import Ball

pygame.init()

def congrats_message(screen, win_text):
    text = WINNER_FONT.render(win_text, 1, WHITE)
    screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, (3 * SCREEN_HEIGHT)//4 - text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000) 

def draw(screen, paddles, ball, color, left_score, right_score):
    left_score_text = SCORE_FONT.render("{}".format(left_score), 1, color)
    right_score_text = SCORE_FONT.render("{}".format(right_score), 1, color)
    
    screen.blit(left_score_text, (SCREEN_WIDTH//4 - left_score_text.get_width()//2, 20))
    screen.blit(right_score_text, (SCREEN_WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(screen, color)

    ball.draw(screen, color)


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.SPEED >= 0: left_paddle.move(up=True)
    elif keys[pygame.K_s] and left_paddle.y + left_paddle.SPEED + left_paddle.height <= SCREEN_HEIGHT: left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.SPEED >= 0: right_paddle.move(up=True)
    elif keys[pygame.K_DOWN] and right_paddle.y + right_paddle.SPEED + left_paddle.height <= SCREEN_HEIGHT: right_paddle.move(up=False)

def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= SCREEN_HEIGHT: ball.y_speed *= -1
    elif ball.y - ball.radius <= 0: ball.y_speed *= -1

    if ball.x_speed < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:

                ball.x_speed *= -1
                ball.y_speed = -1 * calc_y_speed(left_paddle, ball)
    else:  
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:

                ball.x_speed *= -1
                ball.y_speed = -1 * calc_y_speed(right_paddle, ball)

def calc_y_speed(paddle, ball):
    middle_y = paddle.y + paddle.height / 2
    difference_y = middle_y - ball.y
    reduction_factor = (paddle.height / 2) / ball.MAX_SPEED
    y_speed = difference_y / reduction_factor
    
    return y_speed

def reset(left_paddle, right_paddle, ball):
    ball.reset()
    left_paddle.reset()
    right_paddle.reset()


def cat_sight(screen, ball):
    range_ball_x = ceil((NUM_CAT_FRAME * abs(ball.x)) / SCREEN_WIDTH)
    if range_ball_x <= 0: range_ball_x = 1
        
    elif range_ball_x >= 50: range_ball_x = 49  

    bg = pygame.image.load("./asset/background_image/frame-{}.gif".format(range_ball_x))

    pygame.display.update()
    screen.blit(bg, (0,0))
   

def main():
    running = 1
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    bg = pygame.image.load("./asset/background_image/frame-21.gif")

    left_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(SCREEN_WIDTH - 10 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    ball = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, BALL_RADIUS)

    left_score, right_score = 0, 0

    while running:
        clock.tick(FPS)
        
        draw(screen, [left_paddle, right_paddle], ball, WHITE, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()

        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0 or ball.x > SCREEN_WIDTH: 
            if ball.x < 0: right_score += 1
            elif ball.x > SCREEN_WIDTH: left_score += 1
            
            reset(left_paddle, right_paddle, ball)

        won = False
        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
            if left_score >= WINNING_SCORE:
                won = True
                win_text = "Congratulations!!! Left Player"
            elif right_score >= WINNING_SCORE: 
                won = True
                win_text = "Congratulations!!! Right Player"

            congrats_message(screen, win_text)
            
            reset(left_paddle, right_paddle, ball)
            left_score, right_score = 0, 0   

        cat_sight(screen, ball)
    
    pygame.quit()

if __name__ == '__main__': main()