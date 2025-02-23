import turtle
from turtle import Turtle,Screen
from player import Player
from layout import Wall, HorizontalBar, Separator
from ball import Ball
from scoreboard import Scoreboard
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
score_point=Scoreboard((-200,230),'Score')
heart_point=Scoreboard((200,230),'Hearts')

screen.onkeypress(player1.move_left,'Left')
screen.onkeypress(player1.move_right,'Right')

while True:

    ball.ball_move()
    #uderzanie w sciane
    if ball.xcor()>370 or ball.xcor()<-370:
        ball.ball_bounce_x()
    #przejscie za gracza usuniecie serca
    if ball.ycor()<-320:
        heart_point.remove_hearts()
        ball.ball_reset_position()
    # odbijanie sufit
    if ball.ycor()>180:
        ball.ball_bounce_y()
    # odbijanie od gracza
    if ball.distance(player1)<25 and ball.ycor()>-280:
        ball.ball_bounce_y()

# zrobic layout ok
# zrobic movement gracza ok
# zrobic klocki
# zrobic scoreboarda ok
# zrobic odbijanie sie od gracza
# zrobic niszczenie blokow
# zrobic odbijanie sie od scian ok
#





screen.mainloop()

