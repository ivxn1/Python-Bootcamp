from turtle import Turtle, Screen

t = Turtle()

def move():
    t.forward(50)

s = Screen()
s.listen()
s.onkey(key="space", fun=move)

s.exitonclick()