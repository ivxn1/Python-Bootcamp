import random
from turtle import Turtle, Screen

is_race_on = False
winner = None
turtles = []
colors = ["red", 'blue', 'yellow', 'orange', 'purple', 'green']
y_positions = [100, 60, 20, -20, -60, -100]

s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Choose your bet!", prompt="Who do you think is going to win the race? Pick a color: ")
if user_bet:
    is_race_on = True

for i in range(6):
    t = Turtle(shape="turtle")
    t.speed(0)
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    turtles.append(t)

while is_race_on:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() > 230:
            is_race_on = False
            winner = t
            break

winner_color = winner.pencolor()

if winner_color == user_bet:
    print(f"The {winner_color} turtle wins! You won the bet!")
else:
    print(f"The {winner_color} turtle wins! You didn't guess the winner!")

s.exitonclick()
