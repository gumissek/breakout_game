import random
from turtle import  Turtle
import  numpy as np
COLORS = ['pink','green','yellow','blue']
class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks=[]

    def create_brick(self,x_cor,line):
        new_brick=Turtle()

        new_brick.color(random.choice(COLORS))
        new_brick.shape('square')
        new_brick.shapesize(1,2)
        new_brick.penup()
        new_brick.goto(x_cor,160-line*30)
        self.all_bricks.append(new_brick)


    def create_row(self, window_width,line):
        x_cord_list=np.linspace(0 - (window_width / 2), 0 + (window_width / 2), num=int(window_width / 60) + 1)
        for x_cor in x_cord_list:
            self.create_brick(x_cor,line)
    def create_lines(self,window_width,lines:int):
        for line in range(lines):
            self.create_row(window_width,line)