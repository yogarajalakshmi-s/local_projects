# Day - 16 - OOP

# Accessing and modifying object attributes and accessing object methods
# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen
turtle_obj = Turtle()
turtle_obj.shape('turtle')
turtle_obj.color('red', 'green')
turtle_obj.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


# Creating Table
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmandar'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)




# DAY - 19: Event Listeners
from turtle import Turtle, Screen

snoopy = Turtle()
screen = Screen()

def move_forward():
    snoopy.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.exitonclick()


# Functions as Inputs - IMPORTANT
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def calc(n1, n2, func): # -> Higher Order Function
    return func(n1, n2)

print(calc(2, 3, add))


# DAY - 21 : INHERITANCE
class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale. Exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Breathe underwater.")


nemo = Fish()
nemo.breathe()
