from turtle import Turtle

START_POSITON = (0,-280)

class Body(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITON)




    def up(self):
        cor_y = self.ycor() + 10
        self.goto(self.xcor(), cor_y)

    def down(self):
        cor_y = self.ycor() - 10
        self.goto(self.xcor(), cor_y)

    def go_to_start(self):
        self.goto(START_POSITON)