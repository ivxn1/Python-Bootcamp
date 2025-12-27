import turtle
from random import randint
from turtle import Turtle, Screen

def generate_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

turtle.colormode(255)
color_list = [(199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84)]

t = Turtle()
t.speed(0)
y_axis = 0
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(300)
t.setheading(0)
num_dots = 100

for curr_dot in range(1, num_dots + 1):
    t.dot(20, generate_color())
    t.forward(50)

    if curr_dot % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = Screen()
s.exitonclick()