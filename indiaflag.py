import turtle
from turtle import *
import random
# Setup the screen
screen = turtle.Screen()
screen.title("Happy Independence Day")

# Defining a turtle Instance
t = turtle.Turtle()
speed(5)

# Orange Rectangle
def draw_orange_rectangle():
    t.penup()
    t.goto(-200, 125)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.forward(400)
    t.right(90)
    t.forward(84)
    t.right(90)
    t.forward(400)
    t.end_fill()
    t.left(90)
    t.forward(84)

# Green Rectangle
def draw_green_rectangle():
    t.color("green")
    t.begin_fill()
    t.forward(84)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(84)
    t.end_fill()

# Big Blue Circle
def big_blue_circle():
    t.penup()
    t.goto(35, 0)
    t.pendown()
    t.color("navy")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

# Big White Circle
def big_white_circle():
    t.penup()
    t.goto(30, 0)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# Small Blue Circle
def draw_small_blue_circle():
    t.color("navy")
    t.penup()
    t.goto(10, 0)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# The spokes of the flag
def flag_spokes():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(1)
    for i in range(24):
        t.forward(30)
        t.backward(30)
        t.left(15)

# Flag stick
def flag_stick():
    t.color("Brown")
    t.pensize(10)
    t.penup()
    t.goto(-200,125)
    t.right(180)
    t.pendown()
    t.forward(800)

# Text above the flag
def add_text():
    t.penup()
    t.goto(-170, 180)
    t.color("blue")
    t.write("Happy Independence Day", font=("Arial", 24, "bold"))

# Drawing the flag
draw_orange_rectangle()
draw_green_rectangle()
big_blue_circle()
big_white_circle()
draw_small_blue_circle()
flag_spokes()
flag_stick()

# Add text and flower shower after the flag is created
add_text()


turtle.done()
