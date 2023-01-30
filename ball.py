from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_value = 0.1

    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.speed_value *= 0.8

    def restate_pos(self):
        self.setposition(0, 0)
        self.x_bounce()
        self.speed_value = 0.1
