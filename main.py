from turtle import Screen
from ball import Ball
from paddle import Paddle
from wall import Wall
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Breakout')
screen.tracer(0)

ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()


def build_wall(color, n):
    global x, y
    xn = x
    yn = y
    yn -= n
    for i in range(16):
        w = Wall(color)
        if i > 0:
            xn += 50
        w.goto(xn, yn)
        t_wall.append(w)


x = -screen.window_width() / 2 + 25
y = screen.window_height() / 2 - 50

t_wall = []

build_wall('red', 80)
build_wall('orange', 90)
build_wall('green', 100)
build_wall('yellow', 110)
screen.update()


def collision():
    global start_time
    end_time = time.time()
    if end_time - start_time >= 0.3:
        for t in t_wall:
            if ball.distance(t.pos()) < 28:
                t.color('black')
                ball.setheading(ball.next_heading)
                start_time = time.time()
                t.goto(-1000, -1000)
                t_wall.remove(t)
                scoreboard.score += 10
                scoreboard.update_scoreboard()
    else:
        return


def sides_collision():
    x_cor, y_cor = ball.pos()
    x_cor_dis = abs(x_cor) - 400
    if abs(x_cor_dis) < 10:
        ball.setheading(ball.next_heading)
    elif abs(y_cor - 300) < 10:
        ball.setheading(ball.next_heading)


def paddle_collision():
    xcor, ycor = paddle.pos()
    paddle_cor = [(xcor - 50, ycor), (xcor - 25, ycor),
                  (xcor, ycor),
                  (xcor + 25, ycor), (xcor + 50, ycor)]
    if ball.distance(paddle_cor[0]) < 10 or ball.distance(paddle_cor[1]) < 15:
        ball.setheading(135)
    elif ball.distance(paddle_cor[2]) < 15:
        ball.setheading(90)
    elif ball.distance(paddle_cor[3]) < 10 or ball.distance(paddle_cor[4]) < 15:
        ball.setheading(45)


def ball_logic():
    if abs(ball.pos()[1] - 300) <= 20:
        if ball.heading() == 135:
            ball.next_heading = 225
        elif ball.heading() == 45:
            ball.next_heading = 315
        elif ball.heading() == 225:
            ball.next_heading = 135
        elif ball.heading() == 315:
            ball.next_heading = 45
    else:
        if ball.heading() == 90:
            ball.next_heading = 270
        elif ball.heading() == 270:
            ball.next_heading = 90
        elif ball.heading() == 135:
            ball.next_heading = 45
        elif ball.heading() == 315:
            ball.next_heading = 225
        elif ball.heading() == 225:
            ball.next_heading = 315
        elif ball.heading() == 45:
            ball.next_heading = 135


def game_over():
    global game_on
    y_cor = ball.pos()[1]
    if y_cor <= -300:
        scoreboard.game_over()
        paddle.color('black')
        game_on = False


start_time = time.time()

screen.onkeypress(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_right, 'Right')

screen.listen()
game_on = True

while game_on:
    ball_logic()
    collision()
    paddle_collision()
    sides_collision()
    ball.forward(1.5)
    game_over()
    screen.update()

screen.exitonclick()
