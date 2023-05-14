MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ESPRESSO = ['water', 'coffee']
LATTE_OR_CAPPUCCINO = ['water', 'coffee', 'milk']

def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(profit, 2)}")

def ingredients_present(prompt):
    ingredients = ESPRESSO if prompt == 'espresso' else LATTE_OR_CAPPUCCINO
    for ingredient in ingredients:
        resource_needed = MENU[prompt]['ingredients'][ingredient]
        resource_left = resources[ingredient]
        if prompt == 'espresso' and resource_needed > resource_left or prompt == 'latte' and resource_needed > resource_left or prompt == 'cappuccino' and resource_needed > resource_left:
            print(f"Sorry, there is not enough {ingredient}")
            return False
        return True

def resources_present(prompt):
    return ingredients_present(prompt)

def inserted_amount(coins):
    total = 0
    for type in coins:
        if type == 'quarter':
            total += coins[type] * 0.25
        elif type == 'dime':
            total += coins[type] * 0.10
        elif type == 'nickel':
            total += coins[type] * 0.05
        else:
            total += coins[type] * 0.01
    return total

def sufficient_coins(coins, prompt):
    total = inserted_amount(coins)
    money_needed = MENU[prompt]['cost']
    if total > money_needed:
        total -= money_needed
        print(f"Here is ${round(total, 2)} dollars in change.")
    elif total < money_needed:
        return False
    global profit
    profit += total
    return True

def make_coffee(prompt):
    ingredients = ESPRESSO if prompt == 'espresso' else LATTE_OR_CAPPUCCINO
    for ingredient in ingredients:
        resources[ingredient] -= MENU[prompt]['ingredients'][ingredient]

turn_off = False
profit = 0

while not turn_off:
    print("\n\nWelcome 😁!!!")
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == 'report':
        report(profit)
    elif prompt == 'off':
        turn_off = True
    elif resources_present(prompt):
        print("Please insert coins:")
        coin_type = ['quarter', 'dime', 'nickel', 'penny']
        coins = {}
        for type in coin_type:
            coins[type] = int(input(f"How many {type}s: "))
        if sufficient_coins(coins, prompt):
            make_coffee(prompt)
            print(f"Here is your {prompt.title()}. Enjoy!!")
        else:
            print("Sorry, that's not enough money. Money refunded.")

