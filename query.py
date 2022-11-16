### import os    os.system('clear')
import search_and_order_logic
from data import warehouse1, warehouse2
from print_items import printing_warehouses

def get_username():
    while True:
        user_name = input("What is your user name?: ")
        if len(user_name):
            return user_name
        else:
            print('Please input your user name')


def start():
    user_name = get_username()
    print(f"Hello {user_name}!")
    menu(user_name)


def menu(user_name):
    while True:
        
        user_choice = input(
            '\nWhat would you like to do?\n'
            '1. List items by warehouse\n'
            '2. Search an item and place an order\n'
            '3. Quit\n'
            'Type the number of the operation: ')

        if user_choice == '1':
            printing_warehouses()

        elif user_choice == '2':
            search_and_order_logic.search_and_order()

        elif user_choice == '3':
            print(f"Thank you for your visiting {user_name}")
            break

        else:
            print("You can chose only 1 - 3 for now\n")

start()