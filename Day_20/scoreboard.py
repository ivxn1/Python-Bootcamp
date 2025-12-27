from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../../Desktop/data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.setpos(0, 260)
        self.color('white')
        self.hideturtle()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("../../../Desktop/data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0

    def display_score(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.highscore}", align=ALIGNMENT, font=FONT)
