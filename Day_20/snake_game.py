import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('black')
s.title("My snake game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    scoreboard.display_score()
    s.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()

    for segm in snake.snake_segments[1:]:
        if snake.head.distance(segm) < 10:
            scoreboard.reset()
            snake.reset_snake()











s.exitonclick()