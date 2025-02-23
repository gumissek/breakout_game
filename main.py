import random
import time
from turtle import Screen
from player import Player
from layout import Wall, HorizontalBar, Separator
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Breakout by Piotr B.')
screen.listen()
screen.tracer(0)

# tworzenie elementow
player1 = Player()
ball = Ball()
bricks = Brick()
bricks.create_lines(800, 5)
all_bricks = bricks.all_bricks

# tworzenie layoutu
wall_left = Wall('left')
wall_right = Wall('right')
bar = HorizontalBar()
separator = Separator()
score_scoreboard = Scoreboard((-200, 230), 'Score')
hearts_scoreboard = Scoreboard((200, 230), 'Hearts')

screen.onkeypress(player1.move_left, 'Left')
screen.onkeypress(player1.move_right, 'Right')

while hearts_scoreboard.hearts > 0:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()
    if player1.xcor()<-350:
        player1.setx(-350)
    # uderzanie w sciane
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.ball_bounce_x()
    # przejscie za gracza usuniecie serca
    if ball.ycor() < -320:
        hearts_scoreboard.remove_hearts()
        ball.ball_reset_position()
    # odbijanie sufit
    if ball.ycor() > 180:
        ball.ball_bounce_y()
    # odbijanie od gracza
    if ball.distance(player1) < 27 and ball.ycor() < -230:
        ball.ball_bounce_y()
    # odbijanie od cegly
    for brick in all_bricks:
        if brick.distance(ball) < 30:
            # print('ball hits')
            ball.ball_bounce_y()
            ball.move_x += random.randint(-1, 1)
            ball.ball_bounce_x()
            brick.hideturtle()
            all_bricks.remove(brick)
            score_scoreboard.add_point()
            ball.move_speed *= 0.99

# zrobic layout ok
# zrobic movement gracza ok
# zrobic scoreboarda ok
# zrobic odbijanie sie od gracza ok
# zrobic odbijanie sie od scian ok
# zrobic klocki ok
# rozmieszcznie klockow ok
# odbijanie od klockow ok
# zrobic niszczenie blokow ok


screen.exitonclick()
