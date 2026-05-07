from utils import *
import time

# Goal: Get as many points as possible

set_background("summer")

points = 0
happiness = 5
auto = 0

# Sprites 
player = create_sprite("turtle")
player.goto(0, 0)

happy_icon = create_sprite("turtle")
happy_icon.goto(-100, 50)
happy_icon.shapesize(1.5, 1.5)

m1 = create_sprite("turtle")
m1.goto(-200, 200)
m1.hideturtle()


# Controls

def click():
    global points
    points += 1
    player.goto(player.xcor() + 5, player.ycor())

def fun():
    global happiness
    happiness += 1
    player.goto(player.xcor() - 5, player.ycor())

def buy_auto():
    global points, auto
    if points >= 10:
        points -= 10
        auto += 1
        happy_icon.goto(happy_icon.xcor(), happy_icon.ycor() + 5)


window.listen()
window.onkeypress(click, "a")
window.onkeypress(fun, "b")
window.onkeypress(buy_auto, "c")


# Game loop
for i in range(100000000):

    # automatic points
    points += auto * 0.01

    # show score
    m1.clear()
    m1.write("Points: " + str(int(points)) +
             " Happiness: " + str(happiness) +
             " Auto: " + str(auto),
             font=("Arial", 16, "normal"))

    time.sleep(0.01)
    window.update()