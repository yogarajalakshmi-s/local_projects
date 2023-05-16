from turtle import Turtle
DISTANCE = 20
DIRECTION = {'up': 90,  'down': 270, 'left': 180, 'right': 0}

class Snake:

    def __init__(self):  # This snake object contains the turtle objects (the complete snake)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Since we are using self.segments[0] in a lot of places, it is better to create
        # an attribute

    def create_snake(self):
        for i in range(3):
            segment = Turtle(shape='square')
            segment.penup()
            segment.color('white')
            segment.goto(x=(-20 * i), y=0)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):  # Moving 3rd segment's position to 2nd's and 2nd's to 1st
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION['down']:  # We won't allow moving the snake in opposite direction
            # when it's in the same X or Y - axis
            self.head.setheading(DIRECTION['up'])

    def down(self):
        if self.head.heading() != DIRECTION['up']:
            self.head.setheading(DIRECTION['down'])

    def left(self):
        if self.head.heading() != DIRECTION['right']:
            self.head.setheading(DIRECTION['left'])

    def right(self):
        if self.head.heading() != DIRECTION['left']:
            self.head.setheading(DIRECTION['right'])

