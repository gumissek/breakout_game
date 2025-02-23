import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_x = random.randint(-3,3)
        self.move_y = random.randint(-4,4)

        self.setpos(0, -200)

    def ball_move(self):
        self.goto(self.xcor() + self.move_x, self.ycor()+self.move_y)

    def ball_bounce_y(self):
        self.move_y*=-1
    def ball_bounce_x(self):
        self.move_x*=-1

    def ball_reset_position(self):
        self.goto(0,-200)
        self.move_x=abs(self.move_x)
        self.move_y=abs(self.move_y)