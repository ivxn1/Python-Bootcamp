from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.shape('square')
        self.setpos(x=self.x_cor, y=self.y_cor)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


