from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(1, 3)
        self.setpos(0, -250)

    def move_left(self):
        self.goto(self.xcor()-20,self.ycor())
    def move_right(self):
        self.goto(self.xcor()+20,self.ycor())