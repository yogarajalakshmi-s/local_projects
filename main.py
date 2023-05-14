# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
import random
snoopy = Turtle()
snoopy.color('green')

# 1 - Draw a square
for _ in range(4):
    snoopy.forward(100)
    snoopy.right(90)

# 2 - Draw dashed lines
for _ in range(10):
    snoopy.forward(10)
    snoopy.penup()
    snoopy.forward(10)
    snoopy.pendown()

# 3 - Draw different shapes

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def change_color():
    # r = random.random()
    # g = random.random()
    # b = random.random()
    # snoopy.color(r, g, b)
    snoopy.color(random.choice(colours))

for sides in range(3, 11):
    angle = 360 / sides
    for _ in range(sides):
        snoopy.forward(100)
        snoopy.right(angle)
    change_color()


# 4 - Random walk

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
snoopy.width(10)
snoopy.speed('fastest')

def change_color():
    snoopy.color(random.choice(colours))

for _ in range(200):
    snoopy.setheading(random.choice(directions))
    snoopy.forward(30)
    change_color()

# 5 - Random walk - using randomly generated colors

import turtle as t
snoopy = t.Turtle()

directions = [0, 90, 180, 270]
snoopy.width(10)
snoopy.speed('fastest')
t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    snoopy.pencolor((r, g, b))

for _ in range(200):
    snoopy.setheading(random.choice(directions))
    snoopy.forward(30)
    change_color()


# 6 - Spirograph
import turtle as t
snoopy = t.Turtle()

snoopy.speed('fastest')
t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    snoopy.pencolor((r, g, b))

angle = 6
turns = int(360 / angle)
for _ in range(turns):
    snoopy.circle(100)
    snoopy.setheading(snoopy.heading() + angle)
    change_color()


screen = Screen()
screen.exitonclick()



# IMPORTING MODULES

# 1
# import turtle
# tim = turtle.Turle()

# 2
# from turtle import Turtle
# time = Turtle()

# 3
# from turtle import *
# forward(100)

# 4
# import turtle as t
# tim = t.Turtle()

# 5
# import heroes
# print(heroes.gen())
