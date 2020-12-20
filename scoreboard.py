import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(arg=f"Score: {self.score}", font=FONT)
        self.color("black")

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=("Courier", 50, "normal"), align="center")
