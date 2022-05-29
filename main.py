from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))


screen.listen()
screen.onkeypress(paddle1.move_up, 'Up')
screen.onkeypress(paddle1.move_down, 'Down')
screen.onkeypress(paddle2.move_up, 'w')
screen.onkeypress(paddle2.move_down, 's')

ball = Ball()
scoreboard = Scoreboard()
game_on = True
while game_on == True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.pos()[1]) >= 280:
        ball.bounce_y()

    # Detect collision with paddle1
    if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < - 320):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < - 390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

