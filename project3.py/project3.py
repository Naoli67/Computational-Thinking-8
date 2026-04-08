import turtle
import time

# Section1 - Variables
x1, y1 = -200, 180
x2, y2 = -200, 60
x3, y3 = -200, -60
x4, y4 = -200, -180

speed1, speed2, speed3, speed4 = 2, 4, 6, 8
finish_x = 200
# player 4 goes the fastest and will always win and player 3 will be second than player 2 than last is player 1.
# Section2 - Setup
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Race")

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(x1, y1)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(x2, y2)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("green")
t3.penup()
t3.goto(x3, y3)

t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("yellow")
t4.penup()
t4.goto(x4, y4)

s_line = turtle.Turtle()
s_line.hideturtle()
s_line.penup()
s_line.goto(finish_x, 200)
s_line.pendown()
s_line.pensize(5)
s_line.right(90)
s_line.forward(400)

s_line.penup()
s_line.goto(finish_x, 220)
s_line.write("FINISH", align="center", font=("Arial", 16, "bold"))

# Section3 - Racing 
winner = None

for i in range(500):  
    x1 += speed1
    x2 += speed2
    x3 += speed3
    x4 += speed4

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    if x1 >= finish_x:
        winner = 1
        break
    elif x2 >= finish_x:
        winner = 2
        break
    elif x3 >= finish_x:
        winner = 3
        break
    elif x4 >= finish_x:
        winner = 4
        break

    time.sleep(0.1)

# Section4 - Winner
s5 = turtle.Turtle()
s5.hideturtle()
s5.penup()
s5.goto(0, -250)
s5.write(f"Player{winner} wins!", align="center", font=("Arial", 20, "bold"))

screen.mainloop()