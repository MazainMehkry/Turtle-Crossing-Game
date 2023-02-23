from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def levelup(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 30, 'normal'))