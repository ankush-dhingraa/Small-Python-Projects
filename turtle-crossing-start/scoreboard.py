from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-250,260)
        self.write(f"Level : {self.score}",align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER :(",align="center", font=FONT)

