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


# Creting Table
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmandar'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)