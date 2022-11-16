### import os    os.system('clear')
import order
import search
from stock import Stock
from user import User

stock = Stock()

def start():
    user = User()
    user.set_username()
    print(f"Hello {user.user_name}!")
    menu(user.user_name)

def menu(user_name):
    while True:
    
        user_choice = input(
            '\nWhat would you like to do?\n'
            '1. List items by warehouse\n'
            '2. Search an item and place an order\n'
            '3. Quit\n'
            'Type the number of the operation: ')

        if user_choice == '1':
            stock.print_warehouses()

        elif user_choice == '2':
            res = search.search_for_item(stock)
            order.if_order(*res, stock)

        elif user_choice == '3':
            print(f"Thank you for your visiting {user_name}")
            break

        else:
            print("You can chose only 1 - 3 for now\n")

start()