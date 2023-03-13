from data import MENU
from data import resources

if resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["milk"] < \
        MENU["latte"]["ingredients"]["milk"] or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
    print("Sorry! we are out of resources. Please come back next time")
money = 0
game_start = True

'''###def update_ressources(drink):
   update_resources_water = resources["water"] - MENU["drink"]["ingredients"]["water"]
    update_resources_milk = resources["milk"] - MENU["drink"]["ingredients"]["milk"]
    update_resources_coffee = resources["coffee"] - MENU["drink"]["ingredients"]["coffee"]
    resources["water"] = update_resources_water
    resources["milk"] = update_resources_milk
    resources["coffee"] = update_resources_coffee'''

while game_start:
    userInput = input(f"What would you like? (espresso/latte/cappuccino): ")
    if userInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: {money}€")
    elif userInput == "latte" or userInput == "espresso" or userInput == "cappuccino":
        if resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["milk"] < \
                MENU["latte"]["ingredients"]["milk"] or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry! we are out of resources. Please come back next time")
        else:
            print("Please insert money.")
            ein_euro = int(input("How many One euro?: "))
            two_euro = int(input("How many two euro?: "))
            ten_cent = int(input("How many ten Cent?: "))
            twenty_cent = int(input("How many twenty Cent?: "))
            fifty_cent = int(input("How many fifty Cent?: "))
            total_money = (ein_euro * 1) + (two_euro * 2) + (ten_cent * 0.1) + (twenty_cent * 0.2) + (fifty_cent * 0.5)
            if userInput == "latte":
                update_resources_water = resources["water"] - MENU["latte"]["ingredients"]["water"]
                update_resources_milk = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                update_resources_coffee = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["water"] = update_resources_water
                resources["milk"] = update_resources_milk
                resources["coffee"] = update_resources_coffee
                if total_money > MENU["latte"]["cost"]:
                    change = total_money - MENU["latte"]["cost"]
                    money += MENU["latte"]["cost"]
                    print(f"here is your change {change}€")
                    print("Have a great day with you latte! Enjoy!")
                else:
                    print("you havent inert enough money")

            elif userInput == "espresso":
                update_resources_water = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                update_resources_coffee = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                resources["water"] = update_resources_water
                resources["coffee"] = update_resources_coffee
                if total_money > MENU["espresso"]["cost"]:
                    change = total_money - MENU["espresso"]["cost"]
                    money += MENU["espresso"]["cost"]
                    print(f"here is your change {change}€")
                    print("Have a great day with you espresso! Enjoy!")
                else:
                    print("you havent inert enough money")
            elif userInput == "cappuccino":
                update_resources_water = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                update_resources_milk = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                update_resources_coffee = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["water"] = update_resources_water
                resources["milk"] = update_resources_milk
                resources["coffee"] = update_resources_coffee
                if total_money > MENU["cappuccino"]["cost"]:
                    change = total_money - MENU["cappuccino"]["cost"]
                    money += MENU["cappuccino"]["cost"]
                    print(f"here is your change {change}€")
                    print("Have a great day with you cappuccino. Enjoy!")
                else:
                    print("you havent inert enough money")







