from turtle import Turtle
X = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(X, -280)
        self.setheading(90)

    def up(self):
        y = self.ycor() + 20
        self.goto(X, y)


    def res(self):
        self.goto(X, -280)