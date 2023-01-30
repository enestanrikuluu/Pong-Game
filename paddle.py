from turtle import *
from ball import Ball

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(10000)
        self.shape("square")
        self.setposition(position)
        self.shapesize(5, 1)
        self.showturtle()
        self.points = 0

    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)


    def collusion(self, ball):

        if ball.distance(self) < 50 and ball.xcor() > 320 or ball.distance(self) < 50 and ball.xcor() < -320:
            ball.x_bounce()
