from turtle import Turtle


class Padle(Turtle):
    def __init__(self,x,y):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def goup(self):
        self.ny = self.ycor() + 20
        self.goto(self.xcor(), self.ny)

    def godown(self):
        self.ny = self.ycor() - 20
        self.goto(self.xcor(), self.ny)