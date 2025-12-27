import time
from turtle import Screen

from Day_21.scoreboard import Scoreboard
from Day_21.ball import Ball
from paddle import Paddle

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title('Pong Game')
s.tracer(0)

right_p = Paddle(350, 0)
left_p = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(left_p.up, "w")
s.onkey(left_p.down, "s")
s.onkey(right_p.up, "Up")
s.onkey(right_p.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_p) < 50 and ball.xcor() > 320 or ball.distance(left_p) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

s.exitonclick()