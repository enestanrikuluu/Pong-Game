from turtle import Turtle


class ScoreBoardd(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score_board()
    def update_score_board(self):
        self.clear()
        self.goto(-50, 270)
        self.write(self.right_score, align="center", font=('Arial', 20, 'normal'))
        self.goto(+50, 270)
        self.write(self.left_score, align="center", font=('Arial', 20, 'normal'))



    def update_right_score(self):
        self.right_score += 1
        self.update_score_board()

    def update_left_score(self):
        self.left_score += 1
        self.update_score_board()

