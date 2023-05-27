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


# ---------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------
# DAY -24 - Open, Read, Write and Close Files and Absolute and Relative paths

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


# 6. Read file from a different directory - say Desktop - Absolute path
# Replace with the correct username
with open("/Users/{username}/Desktop/file_1.txt") as file:
    contents = file.read()
    print(contents)

# 7. Read file from a different directory - Relative path
# main.py -> path -> /Users/{username}/PycharmProjects/LocalProjects
# In the code, we are going backwards by two folders (../../) i.e., we are going to PycharmProjects from LocalProjects
# And now we are in the Folder {username}. From here, we can trace the path to Desktop and to the required file.
with open("../../Desktop/file_1.txt") as file:
    contents = file.read()
    print(contents)

# ---------------------------------------------------------------------------------------------------------------------

# DAY - 25: READING CSV DATA
# https://pandas.pydata.org/docs/getting_started/index.html#getting-started

with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)

import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)


# ----------------------------------------------------------------------------------------------------------------------

# DAY -26 : LIST AND DICTIONARY COMPREHENSION

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]  # -> list comprehension
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

doubled_list = [n*2 for n in range(1, 5)]
print(doubled_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
shorter_names = [name for name in names if len(name) < 5]  # -> Conditional list comprehension
print(shorter_names)

upcase_names = [name.upper() for name in names if len(name) > 5]
print(upcase_names)


import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
scores = {student: random.randint(1, 100) for student in names}  # -> Dictionary Comprehension
print(scores)

# Conditional dictionary comprehension
passed_students = {student: score for (student, score) in scores.items() if score > 60}
print(passed_students)
