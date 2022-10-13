import sys
from tabulate import tabulate
from zoneinfo import ZoneInfo
from datetime import datetime
zone = ZoneInfo("America/Chicago")
now = datetime.now(tz=zone)
latte_count = 0
expresso_count = 0
reg_count = 0
icebrew_count = 0
special_count = 0
creamer_count = 0
whipped_count = 0
vanilla_count = 0
caramel_count = 0
honey_count = 0
drink_menu = []
extra_menu = []


def main():
    welcome()


def welcome():
    while True:
        banner("Welcome!")
        print(" 1) Drink Menu\n 2) Additives Menu\n 3) Checkout\n 4) Leave\n")
        try:
            enter = int(input("Input: "))
        except ValueError:
            print("--------Invalid option--------")
            continue
        else:
            if enter == 1:
                main_menu()
            elif enter == 2:
                extras_menu()
            elif enter == 3:
                checkout()
            elif enter == 4:
                sys.exit()


def hour_rounder(t):
    return (t.replace(second=t.second, microsecond=0, minute=t.minute))


def banner(sign):
    print("\n|----------------------------------------|")
    print("|         *Azure's Coffee Company*       |")
    print("|                *" + str(sign) + "*              ")
    print("|----------------------------------------|")


def main_menu():
    with open("store_menu.csv") as file:
        for line in file:
            order_n, name, price = line.rstrip().split(",")
            menu = {"Order #": order_n, "Drinks": name, "Price": price}
            drink_menu.append(menu)
    while True:
        banner("Drink menu")
        print(tabulate(drink_menu, headers='firstrow', tablefmt='grid'))
        print(">>Type '0' to Checkout, or type '6' for Extra's Menu<<")
        try:
            drink_order_number = int(input("Enter order #: "))
        except ValueError:
            print("--------Invalid Option--------")
            continue
        if drink_order_number == 1:
            banner("Latte'")
            try:
                quantity = int(input("How many Latte's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 5:
                sys.exit("--------Max:5 per customer--------")
            else:
                global latte_count
                latte_count += quantity
                print(f"Latte's Ordered: {latte_count}")
                continue
        elif drink_order_number == 2:
            banner("Expresso")
            try:
                quantity = int(input("How many Expresso's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 5:
                sys.exit("--------Max:5 per customer--------")
            else:
                global expresso_count
                expresso_count += quantity
                print(f"Expresso's Ordered: {expresso_count}")
                continue
        elif drink_order_number == 3:
            banner("Ice Brew")
            try:
                quantity = int(input("How many Ice Brews would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 5:
                sys.exit("--------Max:5 per customer--------")
            else:
                global icebrew_count
                icebrew_count += quantity
                print(f"Ice Brews Ordered: {icebrew_count}")
                continue
        elif drink_order_number == 4:
            banner("Regular")
            try:
                quantity = int(input("How many Regular's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 5:
                sys.exit("--------Max:5 per customer--------")
            else:
                global reg_count
                reg_count += quantity
                print(f"Regular's Ordered: {reg_count}")
                continue
        elif drink_order_number == 5:
            banner("Special")
            try:
                quantity = int(input("How many Special's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 5:
                sys.exit("--------Max:5 per customer--------")
            else:
                global special_count
                special_count += quantity
                print(f"Special's Ordered: {special_count}")
                continue
        elif drink_order_number == 6:
            extras_menu()
        elif drink_order_number == 0:
            checkout()
        else:
            print("--------Invalid Option---------")
            continue


def extras_menu():
    with open("extras_menu.csv") as file:
        for line in file:
            order_n, name, price = line.rstrip().split(",")
            menu = {"Order #": order_n, "Extra's": name, "price": price}
            extra_menu.append(menu)
    while True:
        banner("Extras")
        print(tabulate(extra_menu, headers='firstrow', tablefmt='grid'))
        print(">>Type '0' to Checkout, or type '6' to go back to the Welcome Menu<<")
        try:
            extras_order_number = int(input("Enter order #: "))
        except ValueError:
            print("--------Invalid Option--------")
            continue
        if extras_order_number == 1:
            banner("Creamer")
            try:
                quantity = int(input("How many Creamer's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 3:
                sys.exit("--------Max:3 per customer--------")
            else:
                global creamer_count
                creamer_count += quantity
                print(f"Creamer's Ordered: {creamer_count}")
                continue
        elif extras_order_number == 2:
            banner("Whip Cream")
            try:
                quantity = int(input("How many Whip Cream's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 3:
                sys.exit("--------Max:3 per customer--------")
            else:
                global whipped_count
                whipped_count += quantity
                print(f"Whip Cream's Ordered: {whipped_count}")
                continue
        elif extras_order_number == 3:
            banner("Vanilla")
            try:
                quantity = int(input("How many Vanilla's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 3:
                sys.exit("--------Max:3 per customer--------")
            else:
                global vanilla_count
                vanilla_count += quantity
                print(f"Vanilla's Ordered: {vanilla_count}")
                continue
        elif extras_order_number == 4:
            banner("Caramel")
            try:
                quantity = int(input("How many Caramel's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 3:
                sys.exit("--------Max:3 per customer--------")
            else:
                global caramel_count
                caramel_count += quantity
                print(f"Caramel's Ordered: {caramel_count}")
                continue
        elif extras_order_number == 5:
            banner("Honey")
            try:
                quantity = int(input("How many Honey's would you like? "))
            except ValueError:
                print("--------Invalid Option--------")
                continue
            if quantity > 3:
                sys.exit("--------Max:3 per customer--------")
            else:
                global honey_count
                honey_count += quantity
                print(f"Honey's Ordered: {honey_count}")
                continue
        elif extras_order_number == 6:
            welcome()
        elif extras_order_number == 0:
            checkout()
        else:
            print("--------Invalid Option--------")
            continue


def checkout():
    print("\nThank you for coming in today!")
    sub = (latte_count * 8) + (expresso_count * 7) + (icebrew_count * 7) + (reg_count * 6) + (special_count * 10) + (creamer_count * .39) + (whipped_count * 0.49) + (vanilla_count * .59) + (caramel_count * 0.69) + (honey_count * 1.19)
    sides_count = whipped_count + caramel_count + vanilla_count + honey_count + creamer_count
    drink_count = latte_count + expresso_count + reg_count + icebrew_count + special_count
    tax = sub * 0.0875
    total = sub + tax
    print("\n|----------------------------------------|")
    print("|         *Azure's Coffee Company*       |")
    print("|----------------------------------------|")
    print("|-----------------RECEIPT----------------|")
    print('|  Drinks: {0}'.format(drink_count))
    print('|  Extras: {0}'.format(sides_count))
    print("|----------------------------------------|")
    print('|  Subtotal: ${:0.2f}'.format(sub))
    print('|  Tax: ${:0.2f}'.format(tax))
    print("|----------------------------------------|")
    print('|  Total: ${:0.2f}'.format(total))
    print("|----------------RECEIPT-----------------|")
    print("|       " + str(hour_rounder(now)))
    print("|----------------------------------------|")
    print("|        *Azure's Coffee Company*        |")
    print("|           *Have a nice day!*           |")
    print("|----------------------------------------|")
    sys.exit()


if __name__ == '__main__':
    main()
