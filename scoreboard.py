from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.goto(-100, 200)
        self.write(self.left_player_score, False, "center", ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_player_score, False, "center", ("Courier", 80, "normal"))

    def l_point(self):
        self.left_player_score += 1
        self.clear()
        self.update_score_board()

    def r_point(self):
        self.right_player_score += 1
        self.clear()
        self.update_score_board()
