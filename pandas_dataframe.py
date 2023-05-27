# DAY - 25: PANDAS LIBRARY

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


# -------------------------------------------------------------------------------------------------------------------
# DAY -26 : PANDA DATAFRAME ITERATION

import pandas

# Iterating over pandas DataFrame - dictionary comprehension
student_dict = {
    'student': ['Angela', 'Jack', 'Lily'],
    'score': [78, 88, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

# Loop through dataframe
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (key, value) in student_data_frame.items():
    print(value)

# Pandas has an in-built loop which iterates through the rows - iterrows
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)


# -------------------------------------------------------------------------------------------------------------------
# DAY - 31: Pandas Dataframe - two attributes
import pandas

# 1. orient='records'
data = pandas.read_csv('french_words.csv')
dict = data.to_dict()
print(dict)
list_of_dict = data.to_dict(orient='records')
print(list_of_dict)

# 2. index=False
# Check flashcard-app in LocalProjects2
# Without index=False, it will add index each time the program runs. That index comes from orient='records'
data = pandas.DataFrame(list_of_dict)
data.to_csv('words_to_learn.csv', index=False)
