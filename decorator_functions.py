# DAY - 54 : Decorators
# 4. Decorator functions - Function that adds a functionality to an existing function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(5)
        function()  # Takes the function name where the decorator is called
        # function()
    return wrapper_function

@delay_decorator  # Decorates the function below with a decorator function
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("Good Day!")


say_hello()  # Hello and Bye have a delay of 5 seconds before printing
say_bye()
say_greeting()  # Has no delay since there is no decorator
# @delay_decorator implies
decorator_func = delay_decorator(say_greeting)  # Here it adds delay to say_greeting since that is the func passed.
decorator_func()


# DAY - 55: DECORATORS WITH *args and **kwargs
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated
def create_new_blog(user):
    print(f"{user.name}'s new blog post!")


new_user = User('Ishu')
new_user.is_logged_in = True
create_new_blog(new_user)
