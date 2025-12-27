import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
c_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c_manager.create_car()
    c_manager.move_cars()

    for c in c_manager.cars:
        if c.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_turtle_finished():
        player.reset_position()
        c_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()