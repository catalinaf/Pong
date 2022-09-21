from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def wall_reset(self):
        self.setposition(0, 0)
        self.paddle_bounce()
