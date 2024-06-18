from turtle import Turtle


class Wall(Turtle):

    def __init__(self, color):
        super().__init__()
        self.fillcolor(color)
        self.shape('square')
        self.shapesize(stretch_wid=0.5, stretch_len=2.5)
        self.penup()



