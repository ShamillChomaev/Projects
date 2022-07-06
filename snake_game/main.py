from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.bgcolor("black")
screen.title("Snake")
screen.setup(width=600,height=600)
screen.tracer(0)

game_true = True
snake = Snake()
food = Food()
score = Score()

while game_true:
    screen.update()
    time.sleep(0.1)
    snake.snake_behaviar()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    if snake.head.distance(food) < 15:
        food.food_create()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset()
        snake.reset_snake()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.reset_snake()
            score.reset()




screen.exitonclick()