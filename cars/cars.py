from turtle import Turtle
import random

CAR_SPEED = 5

COLORS = ["red", "blue", "yellow", "pink", "orange", "brown", "purple"]

class Car():

    def __init__(self):
        self.cars = []
        self.car_speed = CAR_SPEED



    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(260, random.randint(-250, 250),)
            self.cars.append(car)


    def moving(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def more_speed(self):
        self.car_speed += 5