from turtle import Screen
from body import Body
from cars import Car
import time
from scoreboard import Score
screen = Screen()
screen.setup(600,600)
screen.tracer(0)



body = Body()
cars = Car()
board = Score()
board.new_level()
screen.listen()
screen.onkey(body.up, "w")
screen.onkey(body.down, "s")

c = []

game_true = True

while game_true:
    screen.update()
    time.sleep(0.1)
    cars.create_cars()
    cars.moving()

    for car in cars.cars:
        if car.distance(body) < 20:
            game_true = False

    if body.ycor() > 300:
        body.go_to_start()
        cars.more_speed()
        board.increase_level()







screen.exitonclick()