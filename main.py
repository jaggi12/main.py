import turtle

score_a = 0
score_b = 0

# display screen
win = turtle.Screen()
win.setup(900, 700)
win.bgcolor("black")
win.title("Project_Game")
win.tracer()

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.penup()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_len=1, stretch_wid=5)
left_paddle.goto(-430, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.penup()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_len=1, stretch_wid=5)
right_paddle.goto(430, 0)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.dx = 2
ball.dy = 2

# score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("player A:0 player B:0", align="center", font=("Ariel", 20, "normal"))


# moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 20)


def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)


def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)


def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)


win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

while True:
    win.update()
    # ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # ball - wall collision
    # top wall
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1
    # bottom wall
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1
    # right wall
    if ball.xcor() > 440:
        ball.setx(440)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("player A:{} player B:{}".format(score_a, score_b), align="center", font=("Ariel", 20, "normal"))

    # left wall
    if ball.xcor() < -440:
        ball.setx(-440)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("player A:{} player B:{}".format(score_b, score_a), align="center", font=("Ariel", 20, "normal"))

    # collision with paddles
    if ball.xcor() > 430 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -430 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50:
        ball.setx(-390)
        ball.dx *= -1
