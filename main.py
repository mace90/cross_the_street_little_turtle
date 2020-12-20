import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
listofcars = []
speedy = 0.1
for y in range(-250, 250, 20):
    new_car = CarManager(y)
    listofcars.append(new_car)
score = Scoreboard()
print(listofcars)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(speedy)
    screen.update()
    for car in listofcars:
        car.move_the_car()
        if car.xcor() < -200:
            car.reset_the_car()

        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() >= 280:
        player.resetposotion()
        speedy *= 0.9
        score.add_score()


screen.exitonclick()