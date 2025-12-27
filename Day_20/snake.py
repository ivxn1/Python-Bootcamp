from turtle import Turtle

class Snake:
    POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in self.POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape='square')
        t.color('white')
        t.penup()
        t.goto(position)
        self.snake_segments.append(t)

    def extend(self):
        last_segment_pos = self.snake_segments[-1].position()
        self.add_segment(last_segment_pos)

    def move_snake(self):
        for turtles_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[turtles_index - 1].xcor()
            new_y = self.snake_segments[turtles_index - 1].ycor()
            self.snake_segments[turtles_index].goto(new_x, new_y)
        self.snake_segments[0].forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]
