# Reading a file which is not present in our directory - FileNotFound
# with open('file_100.txt') as file:
#     file.read()

# Handling FileNotFound and KeyError Exception
try:
    file = open('file_100.txt')
    dictionary = {'key': 'value'}  # If we didn't specify FileNotFoundError in except,
    # we won't be able to see the Key error when running.
    print(dictionary['key'])  # print(dictionary['key_1']) -> Key Error
except FileNotFoundError:
    file = open('file_100.txt', mode='w')
    file.write('Some Text')
except KeyError as error_message:  # Handling Key error too
    print(f"Key doesn't exist - {error_message}")
else:  # Executes when there is no exception
    content = file.read()
    print(content)
finally:  # Executes irrespective of exceptions
    file.close()


# Raising our own exception
height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError("Human height shouldn't be over 3m")
bmi = weight / height ** 2
print(round(bmi, 2))


# Read, write and update JSON data
import json


dict_1 = {
            'Amazon':
            {
                "email": 'yoga@gmail.com',
                "password": 'fjeur^48748w'
            }
        }
dict_2 = {
            'Twitter':
            {
                "email": 'yoga@gmail.com',
                "password": 'hemciu(er87erc'
            }
        }
try:
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)  # Read json data
except FileNotFoundError:
    with open('data.json', 'w') as data_file:
        json.dump(dict_1, data_file, indent=4)  # Create and write json data, when file is not present
else:
    data.update(dict_2)  # Update json data
    with open('data.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)  # Write in json file with updated data

