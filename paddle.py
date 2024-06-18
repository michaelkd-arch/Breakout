from turtle import Turtle

STARTING_POSITION = (0, -270)


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=0.25, stretch_len=3)
        self.penup()
        self.goto(STARTING_POSITION)
        self.xn = STARTING_POSITION[0]
        self.cor = [self.pos()]

    def move_left(self):
        self.xn -= 20
        self.goto(self.xn, STARTING_POSITION[1])

    def move_right(self):
        self.xn += 20
        self.goto(self.xn, STARTING_POSITION[1])

    def update_cor(self):
        if self.pos() not in self.cor:
            self.cor.append(self.pos())
        for i in self.cor:
            if len(self.cor) > 7:
                if self.pos()[0] - i[0] > abs(30):
                    self.cor.remove(i)
