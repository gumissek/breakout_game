import turtle
from turtle import Turtle,Screen
from player import Player
from layout import Wall, HorizontalBar, Separator
from ball import Ball
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.listen()


player1=Player()
ball=Ball()
#tworzenie layoutu
wall_left=Wall('left')
wall_right=Wall('right')
bar=HorizontalBar()
separator=Separator()


screen.onkeypress(player1.move_left,'Left')
screen.onkeypress(player1.move_right,'Right')

while True:
    ball.ball_move()



# zrobic layout
# zrobic movement gracza ok
# zrobic klocki
# zrobic scoreboarda
# zrobic odbijanie sie od gracza
# zrobic niszczenie blokow
# zrobic odbijanie sie
#





screen.mainloop()

