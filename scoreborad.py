import turtle
from turtle import Turtle,Screen
screen = Screen()
FONT = ("LOUNGE ITALIC ", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=FONT)


    def increase_score(self):
        self.score += 1 #first it will update the score
        self.update_scoreboard()
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as data:
                data.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #            self.goto(0, 0)
    #            self.write("Game over", align="center", font=FONT)


