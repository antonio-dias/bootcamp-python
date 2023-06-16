from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#fff")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.increase_score()

    def increase_score(self, score = 0):
        self.score += score
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)