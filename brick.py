import random
from turtle import  Turtle
import  numpy as np

class Brick(Turtle):
    def __init__(self,window_width):
        super().__init__()
        self.all_bricks=[]
        self.window_width=window_width

    def create_brick(self):
        new_brick=Turtle()
        new_brick.color('white')
        new_brick.shape('square')
        new_brick.shapesize(1,2)
        new_brick.penup()
        new_brick.goto(random.randint(-100,100),100)
        self.all_bricks.append(new_brick)

    def create_wall(self):
        pass