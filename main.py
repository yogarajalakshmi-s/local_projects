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

# DAY - 25: READING CSV DATA & PANDAS LIBRARY
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

# IMPORTANT
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(f"\n{data['temp']}")

# https://pandas.pydata.org/docs/reference/frame.html
# DataFrame conversion to a dictionary
data_dict = data.to_dict()
print(data_dict)

# https://pandas.pydata.org/docs/reference/series.html
# Series conversion to a list
temperature_list = data['temp'].to_list()
print(temperature_list)

# Finding average of the Series
avg_temp = round(sum(temperature_list) / len(temperature_list), 2)
print(avg_temp)
# (or)
print(data['temp'].mean())

# Finding max values of the Series
print(data['temp'].max())

# Getting data in columns
print(data['temp'])
# (or) as an attribute
print(data.temp)

# Getting data from rows
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])  # -> Finding the row with the maximum temperature

# Getting data from a row
monday = data[data.day == 'Monday']
print(monday.temp)
print((monday.temp * 9/5) + 32)  # To Fahrenheit

# Creating a DataFrame from scratch
data_dict_1 = {
    "students": ['A', 'B', 'C'],
    "scores": [98, 99, 100]
}
scores = pandas.DataFrame(data_dict_1)
print(scores)
scores.to_csv('student_data.csv')

# ----------------------------------------------------------------------------------------------------------------------

