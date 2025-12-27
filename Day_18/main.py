import turtle
from turtle import Turtle, Screen
from random import choice, randint
my_turtle = Turtle()
turtle.colormode(255)

my_turtle.speed(0)
my_turtle.shape("turtle")

def generate_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

# for _ in range(4): // MAKE SQUARE SHAPE
#     my_turtle.forward(100)
#     my_turtle.right(90)

# for _ in range(10):  // MAKE DASHED LINE
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# def draw_shape(num_sides):   // MAKE SHAPES FROM TRIANGLE TO DECAGON
#     my_turtle.color(choice(colors))
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
# for i in range(3, 11):
#     draw_shape(i)

# directions = [0, 90 , 180, 270]   // RANDOM WALK
# my_turtle.pensize(10)
# my_turtle.speed(0)
#
# for _ in range(200):
#     my_turtle.color(generate_color())
#     my_turtle.forward(50)
#     my_turtle.setheading(choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        my_turtle.color(generate_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
