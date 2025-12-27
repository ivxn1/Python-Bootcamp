from turtle import Turtle, Screen

t = Turtle()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_anti_clockwise():
    t.left(10)

def move_clockwise():
    t.right(10)

def clear_screen():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

s = Screen()
s.listen()
s.onkey(key="w", fun=move_forwards)
s.onkey(key="s", fun=move_backwards)
s.onkey(key="a", fun=move_anti_clockwise)
s.onkey(key="d", fun=move_clockwise)
s.onkey(key="c", fun=clear_screen)

s.exitonclick()