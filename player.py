import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        newp_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newp_y)

    def resetposotion(self):
        self.goto(STARTING_POSITION)