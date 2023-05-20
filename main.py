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


# DAY -24 - Open, Read, Write and Close Files

# 1. Open, read and close
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# 2.Open and read without need of closing the file. This syntax automatically closes the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# 3. Write in a file. (Replaces all contents)
with open("my_file.txt", mode='w') as file:
    file.write("New Text.")

# 4. Write in a file without clearing the previous content
with open("my_file.txt", mode='a') as file:
    file.write("\nHello World! My name is Yoga!")

# 5. If we mention a non-existing file in write mode, it creates that file
with open("new_file.txt", mode='w') as file:
    file.write("My new file!")





