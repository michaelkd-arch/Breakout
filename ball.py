from turtle import Turtle

STARTING_POSITION = (0, -260)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=0.5)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.next_heading = 0

