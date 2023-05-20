# https://docs.python.org/3/library/turtle.html

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # Tracer is turned off - Implies there will be no animation shown on the screen

snake = Snake()
food = Food()
score = Score()

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
    snake.move()  # TODO: Check why it shows error when we stop the game

    # Detecting collision with the food
    if snake.head.distance(food) < 20:
        food.reset_location()
        score.increase_score()
        snake.extend()

    # Detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset()

    # Detecting collision with the tail
    for segment in snake.segments[1:]:  # Since we are comparing the head segment with other segments,
        # we don't have to loop through the head index, so slicing it off
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset()

screen.exitonclick()
