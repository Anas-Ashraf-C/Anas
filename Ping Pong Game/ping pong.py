# import library module
import turtle # import turtle
# import time # import time

# Initialize screen
wind = turtle.Screen()
wind.title("Ping Pong By Go</>Code")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)  # Stop auto updating

# Madrab 1 (Player 1)
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350, 0)

# Madrab 2 (Player 2)
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = .3

# Score setup
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0  Player2: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def madrab1_up():
    y = madrab1.ycor()
    if y < 250:
        y += 20
        madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    if y > -250:
        y -= 20
        madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    if y < 250:
        y += 20
        madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    if y > -250:
        y -= 20
        madrab2.sety(y)

# Keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

# Main game loop
while True:
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player1: {}  Player2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player1: {}  Player2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (-350 < ball.xcor() < -340) and (madrab1.ycor() - 50 < ball.ycor() < madrab1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    if (340 < ball.xcor() < 350) and (madrab2.ycor() - 50 < ball.ycor() < madrab2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
    
