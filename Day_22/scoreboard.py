from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 260)
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!",align='center', font=FONT)

