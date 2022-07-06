from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.hideturtle()
        self.goto(-200, 250)


    def new_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_level(self):
        self.score += 1