### import os    os.system('clear')
import search
from user import User
import stock


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
            '3. Browse by category\n'
            '4. Quit\n'
            'Type the number of the operation: ')

        if user_choice == '1':
            stock.print_items()

        elif user_choice == '2':
            search.search_for_item()

        elif user_choice == '3':
            search.search_by_category()

        elif user_choice == '4':
            print(f"Thank you for your visiting {user_name}")
            break

        else:
            print("You can chose only 1 - 3 for now\n")

if __name__ == '__main__':
    start()