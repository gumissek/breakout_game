import turtle
from turtle import Turtle,Screen
from player import Player
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.listen()


player1=Player()

screen.onkeypress(player1.move_left,'Left')
screen.onkeypress(player1.move_right,'Right')




# zrobic layout
# zrobic movement gracza ok
# zrobic klocki
# zrobic scoreboarda
# zrobic odbijanie sie od gracza
# zrobic niszczenie blokow
# zrobic odbijanie sie
#





screen.mainloop()

