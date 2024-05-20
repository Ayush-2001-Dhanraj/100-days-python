from data import MENU, resources
import math

money = 0
chosen_option = input("What would you like? (espresso/latte/cappuccino):")


def generate_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")


def check_resources(option):
    if option not in ["espresso", "latte", "cappuccino"]:
        return False

    is_sufficient = True

    for ingredient, value in MENU[option]['ingredients'].items():
        if resources[ingredient] < value:
            print(f"Sorry there is not enough {ingredient}.")
            is_sufficient = False

    return is_sufficient


def process_transaction(option):
    global money
    print("Please insert coins.")
    quarters = int(input("how many Quarters?: "))
    dimes = int(input("how many Dimes?: "))
    nickles = int(input("how many Nickles?: "))
    pennies = int(input("how many Pennies?: "))

    entered_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    if entered_amount < MENU[option]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        for ingredient, value in MENU[option]['ingredients'].items():
            resources[ingredient] -= value
        money += MENU[option]['cost']
        print(f"Here is ${round(entered_amount - MENU[option]['cost'], 2)} in change.")
        print(f"Here is your {option} ☕. Enjoy!")


def process_order(option):
    if check_resources(option):
        process_transaction(option)


while chosen_option != "off":
    if chosen_option == "report":
        generate_report()
    else:
        process_order(chosen_option)

    chosen_option = input("What would you like? (espresso/latte/cappuccino):")

