from cli.loader import Loader
from classes import User

personnel = Loader(model="personnel")
stock = Loader(model="stock")


def start():
    sign_in_choice = input('Hello user:\n'
                           '1. Sign in as user\n'
                           '2. Sign in as guest\n'
                           '3. Exit warehouse\n')
    user = None

    if sign_in_choice == '1':
        user = user_name_pass()
    elif sign_in_choice == '2':
        user = User()
    elif sign_in_choice == '3':
        print('Thank you for visiting')

    if user:
        menu(user)


def authenticate(name, password):
    for employee in personnel:
        if employee.is_named(name):
            if employee.authenticate(password):
                return employee
    user = User()
    return user


def user_name_pass():
    again = '1'
    while again == '1':
        user_name = input('What is your user name?: ')
        password = input('What is your password?: ')
        user = authenticate(user_name, password)

        if user.is_authenticated:
            return user
        else:
            again = input('User name or password is incorrect\n'
                          'Try again?: 1\n'
                          'Sign in as guest: 2\n')
        if again == '2':
            print('You are logged in as Guest')
            return user


def searched_items(item):
    found_items = []
    for warehouse in stock:
        found_items.extend(warehouse.search(item))
    return found_items


def menu(user):
    user.greet()
    while True:

        user_choice = input(
            '\nWhat would you like to do?\n'
            '1. List items by warehouse\n'
            '2. Search an item and place an order\n'
            '3. Quit\n'
            'Type the number of the operation: ')

        if user_choice == '1':
            for warehouse in stock:
                warehouse.print_items()
            number_all_items = 0
            for warehouse in stock:
                number_all_items += warehouse.occupancy()
                print(f'Warehouse: {warehouse.warehouse_id}: {warehouse.occupancy()}ea')
            if user.is_authenticated:
                user.add_to_history(f'You were listing all items and {number_all_items} items was listed')

        elif user_choice == '2':
            item = input('What are you looking for: ')
            found_items = searched_items(item)
            if found_items:
                for item in found_items:
                    print(f'Warehouse: {item.warehouse_id}, {item}, on stock since: {item.date_of_stock}')
            else:
                print('Unfortunately the given item was not found in the stock')

            if user.is_authenticated:
                user.add_to_history(f'Your were looking for {item} and {len(found_items)}ea were found')
                order_menu(user, found_items[-1])

        elif user_choice == '3':
            if user.is_authenticated:
                print('Your history of search: ')
                user.print_history()
            user.bye()
            break

        else:
            print("You can chose only 1 - 3 for now\n")


def order_menu(user, item):
    order = input('Would you like to order this item? y/n: ')
    if order == 'y':
        amount = input('How many items would you like to order?: ')
        order = user.order(item, int(amount))
        print(order)
        user.add_to_history(order)


if __name__ == '__main__':
    start()
