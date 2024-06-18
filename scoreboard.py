from turtle import Turtle

FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.level = 1
        self.score = 0
        self.penup()
        self.goto(-400, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align='left', font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write('Game Over', align='left', font=FONT)
