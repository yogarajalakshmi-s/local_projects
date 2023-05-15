# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

snoopy = Turtle()
screen = Screen()

def forward():
    snoopy.forward(20)

def backward():
    snoopy.backward(20)

def clockwise():
    snoopy.setheading(snoopy.heading() - 20)
    # (or) snoopy.right(10)

def counter_clockwise():
    snoopy.setheading(snoopy.heading() + 20)

def clear_screen():
    snoopy.reset()
    # (or)
    # snoopy.clear()
    # snoopy.penup()
    # snoopy.home()
    # snoopy.pendown()

screen.listen()
screen.onkey(key='W', fun=forward)
screen.onkey(key='S', fun=backward)
screen.onkey(key='A', fun=clockwise)
screen.onkey(key='D', fun=counter_clockwise)
screen.onkey(key='C', fun=clear_screen)
screen.exitonclick()
