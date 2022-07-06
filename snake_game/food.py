from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.food_create()



    def food_create(self):
        x_coor = random.randint(-260,260)
        y_coor = random.randint(-260,260)
        self.goto(x_coor,y_coor)