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

