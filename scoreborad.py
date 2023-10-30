import turtle
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    def update_scoreboard(self):
       self.write(f"Score: {self.score}", False, align="center", font=FONT)


    def increase_score(self):
        self.score += 1 #first it will update the score
        self.clear()
        self.update_scoreboard()


