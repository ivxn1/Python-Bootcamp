from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while True:
    action = input(f"What would you like? ({my_menu.get_items()}): ")
    if action == 'off':
        break
    elif action == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(action)
        if my_coffee_maker.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)