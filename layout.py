from turtle import Turtle

class Wall(Turtle):
    def __init__(self,side:str):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(30,1)
        if side=='left':
            self.setpos(-390,0)
        elif side=='right':
            self.setpos(390,0)

class HorizontalBar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(1,40)
        self.setpos(0,200)

class Separator(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1)
        self.setpos(0,250)