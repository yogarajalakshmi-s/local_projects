from turtle import Turtle
import random


class Food(Turtle): #  Inheriting the Turtle class
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.penup()
        self.speed('fastest')
        self.reset_location()

    def reset_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 260))  # Screen size is 600,so it will be -300 to 300.
        # But using 300 for rand will hit the wall, so reducing the number to 280
        # And y-axis is limited to 260 because of scoreboard

