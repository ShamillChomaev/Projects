from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

paad_r = Paddle((350,0))
paad_l = Paddle((-350,0))
ball = Ball()
scoree = Scoreboard()


screen.listen()
screen.onkey(paad_l.up, "w")
screen.onkey(paad_l.down, "s")
screen.onkey(paad_r.up, "Up")
screen.onkey(paad_r.down, "Down")

game_true = True

while game_true:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.move2()
    if ball.distance(paad_r) < 100 and ball.xcor() > 320 or ball.distance(paad_l) < 100 and ball.xcor() > -320:
        ball.move3()

    if ball.xcor() > 380:
        scoree.l_point()
        ball.reset()
    elif ball.xcor() < -380:
        scoree.r_point()
        ball.reset()



screen.exitonclick()