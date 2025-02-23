from turtle import Turtle
FONT =('Courier', 25, 'normal')
ALIGNMENT = 'center'



class Scoreboard(Turtle):
    def __init__(self,postition,text):
        super().__init__()
        self.text=text
        self.hideturtle()
        self.color('white')
        self.penup()
        self.setpos(postition)
        self.score=0
        self.hearts=3
        if self.text=='Score':
            self.refresh_score()
        elif self.text=='Hearts':
            self.refresh_hearts()

    def refresh_score(self):
        self.write(f'{self.text}:{self.score}',move=False,font=FONT,align=ALIGNMENT)
    def refresh_hearts(self):
        self.write(f'{self.text}:{self.hearts}',move=False,font=FONT,align=ALIGNMENT)

    def add_point(self):
        self.clear()
        self.score+=1
        self.refresh_score()

    def remove_hearts(self):
        self.clear()
        self.hearts-=1
        self.refresh_hearts()