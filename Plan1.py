import os
import turtle
import time
import random

delay = 0.3


# set up the screen
window = turtle.Screen()
window.title("snake game")
window.bgcolor("red")
window.setup(width=600, height=600)
window.tracer(0)
# Snake_head
Snake_head = turtle.Turtle()
Snake_head.speed(0)
Snake_head.shape("circle")
Snake_head.color("yellow")
Snake_head.penup()
Snake_head.goto(0, 0)
Snake_head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(0, 0)
arr = []
#points before the game starts
start_score = 0;
high_score = 0;

#score
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("SCORE: 0 HIGH SCORE: 0", align="center", font=("Arial", 25," bold"))


# functions

def move_up():
    if Snake_head.direction != "down":
        Snake_head.direction = "up"

def move_down():
    if Snake_head.direction != "up":
     Snake_head.direction = "down"


def move_left():
    if Snake_head.direction != "right":
     Snake_head.direction = "left"


def move_right():
    if Snake_head.direction != "left":
     Snake_head.direction = "right"


def move():
    if Snake_head.direction == "up":
        y = Snake_head.ycor()
        Snake_head.sety(y + 20)
    if Snake_head.direction == "down":
        y = Snake_head.ycor()
        Snake_head.sety(y - 20)
    if Snake_head.direction == "left":
        x = Snake_head.xcor()
        Snake_head.setx(x - 20)
    if Snake_head.direction == "right":
        x = Snake_head.xcor()
        Snake_head.setx(x + 20)

# keybord-bindings
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, 'Down')
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

while True:

    window.update()
    i = 290
    if Snake_head.xcor()> i or Snake_head.xcor()<-i or Snake_head.ycor() > i or Snake_head.ycor()<-i:
        time.sleep(1)
        Snake_head.goto(0, 0)
        Snake_head.direction = "stop"
        print("game Over")

    if Snake_head.distance(food) < 20:
        x = random.randint(-i, i)
        y = random.randint(-i, i)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        arr.append(new_segment)
        #change score
        start_score += 100

        if start_score > high_score:
            high_score = start_score
        score.clear()
        score.write("SCORE: {} HIGH SCORE: {}".format(start_score,high_score), align="center", font=("Arial", 25, " bold"))

    # add body to the snake
    for index in range(len(arr) - 1, 0, -1):
        x = arr[index - 1].xcor()
        y = arr[index - 1].ycor()
        arr[index].goto(x, y)

    if len(arr) > 0:
        x = Snake_head.xcor()
        y = Snake_head.ycor()
        arr[0].goto(x, y)

    move()
    #collision with
    for segment in arr:
        if segment.distance(Snake_head) < 20:
            time.sleep(1)
            Snake_head.goto(0, 0)
            Snake_head.direction = "stop"
            for segment in arr:
                segment.goto(2000, 2000)
            arr.clear()
            start_score=0
            score.clear()
            score.write("SCORE: {} HIGH SCORE: {}".format(start_score, high_score), align="center",
                        font=("Arial", 25, " bold"))

    time.sleep(delay)





