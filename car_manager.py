import turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(turtle.Turtle):
    def __init__(self, y_starting_cor):
        super(CarManager, self).__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.tempo = MOVE_INCREMENT
        self.goto(random.randrange(300, 600, STARTING_MOVE_DISTANCE), y_starting_cor)

    def move_the_car(self):
        new_x = self.xcor() + self.tempo * -1
        self.goto(new_x, self.ycor())

    def reset_the_car(self):
        reset_x = random.randrange(300, 600, STARTING_MOVE_DISTANCE)
        self.goto(reset_x, self.ycor())


