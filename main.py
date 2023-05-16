# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # Tracer is turned off - Implies there will be no animation shown on the screen

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_over = False
while not game_over:
    screen.update()  # used when tracer is off - turns on the animation after the move is complete and
    # refreshes the screen with the updated movement
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
