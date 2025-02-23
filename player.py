from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(0.5, 3)
        self.setpos(0, -240)

    def move_left(self):
        self.goto(self.xcor()-10,self.ycor())
    def move_right(self):
        self.goto(self.xcor()+10,self.ycor())