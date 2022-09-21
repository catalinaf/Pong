import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.left_player_up, "w")
screen.onkey(paddle.left_player_down, "s")
screen.onkey(paddle.right_player_up, "Up")
screen.onkey(paddle.right_player_down, "Down")

game_is_on = True
sleep_time = 0.08
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(sleep_time)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(paddle.right_player) < 50 and ball.xcor() > 320 or
            ball.distance(paddle.left_player) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()
        sleep_time *= 0.9

    if ball.xcor() > 380:
        ball.wall_reset()
        sleep_time = 0.08
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.wall_reset()
        sleep_time = 0.08
        scoreboard.r_point()

screen.exitonclick()
