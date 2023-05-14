from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False

coffee_maker_obj = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while not turn_off:
    print("Welcome 😁😁 !!!")
    prompt = input(f"What would you like? ({menu.get_items()}): ").lower()
    if prompt == 'report':
        coffee_maker_obj.report()
        money.report()
    elif prompt == 'off':
        turn_off = True
    else:
        drink = menu.find_drink(prompt)
        if coffee_maker_obj.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)
