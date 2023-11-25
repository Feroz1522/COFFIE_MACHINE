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

MONEY = 0


# TODO : 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def user_input():
    customer_input = input("what would you like? (espresso/latte/cappuccino)").lower()
    return customer_input


def insert_coin():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    quarters_input = int(input("How many quarters ? $"))
    dimes_input = int(input("How many dimes ? $"))
    nickles_input = int(input("How many nickles ? $"))
    pennies_input = int(input("How many pennies ? $"))
    total = (quarters * quarters_input) + (dimes * dimes_input) + (nickles_input * nickles) + (pennies * pennies_input)
    return round(total,2)


def latte():
    resources['water'] -= MENU['latte']['ingredients']['water']
    resources['milk'] -= MENU['latte']['ingredients']['milk']
    resources['coffee'] -= MENU['latte']['ingredients']['coffee']


def making_latte():
    global MONEY
    cash_deposited = insert_coin()

    if cash_deposited == MENU['latte']['cost']:
        latte()
        MONEY += MENU['latte']['cost']
        print("Thank You, Enjoy Your Latte . ComeBack Again")
    elif cash_deposited <= MENU['latte']['cost']:
        print(f"Not having enough Money. Refund money {cash_deposited}")
    elif cash_deposited >= MENU['latte']['cost']:
        latte()
        MONEY += MENU['latte']['cost']
        balance_money = cash_deposited - MENU['latte']['cost']
        print(f"Thank You, Enjoy Your Latte. ComeBack Again")
        print(f"Have Your balance ${balance_money}.")


def espresso():
    resources['water'] -= MENU['espresso']['ingredients']['water']
    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']


def making_espresso():
    global MONEY
    MONEY += MENU['espresso']['cost']
    cash_deposited = insert_coin()

    if cash_deposited == MENU['espresso']['cost']:
        espresso()
        MONEY += MENU['espresso']['cost']
        print("Thank You, Enjoy Your Latte . ComeBack Again")
    elif cash_deposited <= MENU['espresso']['cost']:
        print(f"Not having enough Money. Refund money {cash_deposited}")
    elif cash_deposited >= MENU['espresso']['cost']:
        espresso()
        MONEY += MENU['espresso']['cost']
        balance_money = cash_deposited - MENU['espresso']['cost']
        print(f"Thank You, Enjoy Your Espresso. ComeBack Again")
        print(f"Have Your balance ${balance_money}.")


def cappuccino():
    resources['water'] -= MENU['cappuccino']['ingredients']['water']
    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']


def making_cappuccino():
    global MONEY
    MONEY += MENU['cappuccino']['cost']
    cash_deposited = insert_coin()

    if cash_deposited == MENU['cappuccino']['cost']:
        cappuccino()
        MONEY += MENU['cappuccino']['cost']
        print("Thank You, Enjoy Your Latte . ComeBack Again")
    elif cash_deposited <= MENU['cappuccino']['cost']:
        print(f"Not having enough Money. Refund money {cash_deposited}")
    elif cash_deposited >= MENU['cappuccino']['cost']:
        cappuccino()
        MONEY += MENU['cappuccino']['cost']
        balance_money = cash_deposited - MENU['cappuccino']['cost']
        print(f"Thank You, Enjoy Your Cappuccino. ComeBack Again")
        print(f"Have Your balance ${balance_money}.")


machine_status = True
while machine_status:
    stock = resources
    user_respond = user_input()
    # TODO : 2.Turn off the Coffee Machine by entering “off” to the prompt.
    if user_respond == "off":
        print("machine turned off")
        machine_status = False
    # TODO : 3. Print report
    elif user_respond == "report":
        print(f" water : {resources['water']} \n milk : {resources['milk']} \n coffee : {resources['coffee']} \n"
              f" money : ${MONEY}")
    # TODO : 4.Check resources sufficient?
    elif user_respond == "latte":
        if stock["water"] <= MENU['latte']['ingredients']['water']:
            print("Sorry ! There is no water.")
        elif stock["milk"] <= MENU['latte']['ingredients']['milk']:
            print("Sorry ! There is no milk")
        elif stock["coffee"] <= MENU['latte']['ingredients']['coffee']:
            print("Sorry ! There is no coffee")
        else:
            making_latte()

    # making espresso
    elif user_respond == "espresso":
        if stock["water"] <= MENU['espresso']['ingredients']['water']:
            print("Sorry ! There is no water.")
        elif stock["coffee"] <= MENU['espresso']['ingredients']['coffee']:
            print("Sorry ! There is no coffee")
        else:
            making_espresso()

    # making cappuccino
    elif user_respond == "cappuccino":
        if stock["water"] <= MENU['cappuccino']['ingredients']['water']:
            print("Sorry ! There is no water.")
        elif stock["milk"] <= MENU['cappuccino']['ingredients']['milk']:
            print("Sorry ! There is no milk")
        elif stock["coffee"] <= MENU['cappuccino']['ingredients']['coffee']:
            print("Sorry ! There is no coffee")
        else:
            making_cappuccino()
    else:
        print("Invalid Data ! enter properly")
