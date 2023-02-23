from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
X = 310


class Cars:

    def __init__(self):
        self.car = []
        self.car_speed = 5

    def rand(self):
        x = random.randint(1, 6)
        if x == 1:
            cars = Turtle()
            cars.shape("square")
            cars.color(random.choice(COLORS))
            cars.penup()
            cars.shapesize(1, 2)
            ry = random.randint(-220, 230)
            cars.goto(X, ry)
            self.car.append(cars)

    def move(self):
        for cars in self.car:
            cars.backward(self.car_speed)

    def clear(self):
        # for cars in self.car:
        #     cars.hideturtle()
        # self.car.clear()
        self.car_speed += 5