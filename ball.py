from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_s=0.1

    def move(self):
        nx=self.xcor()+self.xmove
        ny=self.ycor()+self.ymove
        self.goto(nx,ny)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_s *=0.9

    def rest_p(self):
        self.goto(0,0)
        time.sleep(0.1)
        self.move_s=0.1
        self.bounce_x()