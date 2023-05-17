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
        for i in range(3):  # Creating a 3-segment length snake
            self.add_segment(-20 * i, 0)

    def add_segment(self, x_cor, y_cor):
        segment = Turtle(shape='square')
        segment.penup()
        segment.color('white')
        segment.goto(x=x_cor, y=y_cor)
        self.segments.append(segment)

    # Increasing tail length
    def extend(self):
        last_segment = self.segments[-1]
        self.add_segment(last_segment.xcor(), last_segment.ycor())  # Creating a new segment with the last segment's position

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
