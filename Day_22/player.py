from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.reset_position()
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_turtle_finished(self):
        if self.ycor() >= 280:
            return True
        else:
            return False