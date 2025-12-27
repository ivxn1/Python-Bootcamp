import turtle
from turtle import Turtle, Screen

import pandas

guess = 0
total_states = 50
image = "blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)
turtle.penup()


states_data = pandas.read_csv("50_states.csv")
all_states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} States Guessed!",
                                    prompt="What's another state's name?:").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states_list:
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()

        current_state_data = states_data[states_data.state == answer_state]
        state_x = current_state_data.x.item()
        state_y = current_state_data.y.item()
        state_turtle.goto(state_x, state_y)
        state_turtle.write(current_state_data.state.item())
        guessed_states.append(answer_state)

states_not_guessed = [st for st in all_states_list if st not in guessed_states]
states_not_guessed_table = pandas.DataFrame(states_not_guessed)
states_not_guessed_table.to_csv("not_guessed_states.csv")