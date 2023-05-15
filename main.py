# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title='Turtle race game', prompt='Which turtle would win the race? (Enter the color): ')

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []

if guess:
    race = True

    for i in range(7):
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=(-100 + (i * 30)))
        turtles.append(new_turtle)


while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winning_turtle = turtle.pencolor()
            if guess == winning_turtle:
                print(f"You've won! The winning turtle is {winning_turtle}")
            else:
                print(f"You've lost. The winning turtle is {winning_turtle}")

        distance = random.randint(0, 10)  # Inclusive of both 0 and 10
        turtle.forward(distance)


screen.exitonclick()

