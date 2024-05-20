from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

shop_menu = Menu()
shop_coffee_maker = CoffeeMaker()
shop_money_machine = MoneyMachine()

choice = input(f"What would you like? {shop_menu.get_items()}")

while choice != "off":
    if choice == 'report':
        shop_coffee_maker.report()
        shop_money_machine.report()
    else:
        drink = shop_menu.find_drink(choice)
        if drink:
            if shop_coffee_maker.is_resource_sufficient(drink) and shop_money_machine.make_payment(drink.cost):
                shop_coffee_maker.make_coffee(drink)

    choice = input(f"What would you like? {shop_menu.get_items()}")