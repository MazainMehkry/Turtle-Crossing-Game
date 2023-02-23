from turtle import Screen
from player import Player
from cars import Cars
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Game")

player = Player()
car1 = Cars()
score = Score()

screen.listen()
screen.onkeypress(player.up, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    score.update()
    car1.rand()
    car1.move()

    if player.ycor() > 280:
        player.res()
        car1.clear()
        score.levelup()
    for cars in car1.car:
        if cars.distance(player) < 20:
            game_on = False
            score.game_over()


screen.exitonclick()