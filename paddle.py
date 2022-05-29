from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.position = position
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.goto(self.position[0], self.position[1])

    def move_up(self):
        self.goto(self.pos()[0], self.pos()[1] + 15)

    def move_down(self):
        self.goto(self.pos()[0], self.pos()[1] - 15)
