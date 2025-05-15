from turtle import Screen
from paddle import Paddle
from ball import Ball
from pongscore import Scoreboard
import time

screen = Screen()
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

sleep_timer = 0.1
game_on = True
screen.setup(800,600)
screen.title("Pong")
screen.bgcolor("black")


screen.listen()


screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right and left paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() >320 or
        ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()


    if  ball.xcor() >380:
        ball.reset_pos()
        score.l_point()

    if  ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()






screen.exitonclick()