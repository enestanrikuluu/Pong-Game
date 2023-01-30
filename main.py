from turtle import *
from paddle import Paddle
from ball import Ball
import time
from Scoreboard import ScoreBoardd

my_turtle = Turtle()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)





paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))



screen.onkeypress(paddle_right.up, 'Up')
screen.onkeypress(paddle_right.down, 'Down')
screen.onkeypress(paddle_left.up, 'w')
screen.onkeypress(paddle_left.down, 's')

screen.listen()

ball = Ball()
score_board = ScoreBoardd()
game = True

while game:
    time.sleep(ball.speed_value)
    screen.update()
    ball.move()
    if abs(ball.ycor()) >= 290:
        ball.y_bounce()
    paddle_right.collusion(ball)
    paddle_left.collusion(ball)
    if ball.xcor() >= 390:
        score_board.update_left_score()
        ball.restate_pos()
    if ball.xcor() <= -390:
        score_board.update_right_score()
        ball.restate_pos()





screen.exitonclick()
