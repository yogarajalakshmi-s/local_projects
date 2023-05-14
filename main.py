# https://docs.python.org/3/library/turtle.html

import turtle as t
import colorgram
import random

snoopy = t.Turtle()

def get_colors():
    rgb_colors = []
    colors = colorgram.extract('hirst_spot_painting_1.jpg', 30)
    for color in colors:
        rgb_color = color.rgb
        rgb_colors.append((rgb_color.r, rgb_color.g, rgb_color.b))
    return rgb_colors


# Setting initial position
snoopy.hideturtle()
snoopy.setheading(225)
snoopy.penup()
snoopy.forward(300)
snoopy.speed('fastest')
t.colormode(255)
colors = get_colors()

snoopy.setheading(0)

def spot_paint():
    for _ in range(10):
        snoopy.dot(20, random.choice(colors))
        snoopy.penup()
        if _ != 9:
            snoopy.forward(50)

for _ in range(10):
    spot_paint()
    snoopy.setheading(90)
    snoopy.penup()
    snoopy.forward(50)
    snoopy.setheading(180)
    snoopy.forward(450)
    snoopy.setheading(0)

my_screen = t.Screen()
my_screen.exitonclick()
