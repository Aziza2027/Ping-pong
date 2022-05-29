import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        #self.speed(1)
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(self.pos()[0] + self.x, self.pos()[1] + self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def reset_position(self):
        time.sleep(0.5)
        self.goto(0, 0)
        self.bounce_x()