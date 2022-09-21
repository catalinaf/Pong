from turtle import Turtle

POSITIONS = [(-350, 0), (350, 0)]
UP = 90
MOVE_DISTANCE = 20


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()
        self.left_player = self.paddles[0]
        self.left_player.setheading(UP)
        self.right_player = self.paddles[1]
        self.right_player.setheading(UP)

    def create_paddle(self):
        for position in POSITIONS:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.turtlesize(1, 5)
            paddle.up()
            paddle.speed("fastest")
            paddle.goto(position)
            self.paddles.append(paddle)

    def left_player_up(self):
        self.left_player.forward(MOVE_DISTANCE)

    def left_player_down(self):
        self.left_player.backward(MOVE_DISTANCE)

    def right_player_up(self):
        self.right_player.forward(MOVE_DISTANCE)

    def right_player_down(self):
        self.right_player.backward(MOVE_DISTANCE)
