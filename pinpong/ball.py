from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor,y_cor)

    def move2(self):
        self.y_move *= -1

    def move3(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def reset(self):
        self.goto(0,0)
        self.move3()
