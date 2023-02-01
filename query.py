import search
from user import User
import stock
from cli.data import personnel


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


def user_name_pass():
    again = '1'
    while again == '1':
        user_name = input('What is your user name?: ')
        password = input('What is your password?: ')
        if checker(personnel, user_name, password):
            return User(user_name, password)
        else:
            again = input('User name or password is incorrect\n'
                          'Try again?: 1\n'
                          'Sign in as guest: 2\n')
    if again == '2':
        print('You are logged in as Guest')
        return User()


def checker(lst, user, password):
    for dic in lst:
        if dic.get('user_name') == user and dic.get('password') == password:
            return True
        elif dic.get('head_of') is not None:
            if checker(dic['head_of'], user, password):
                return True
    return False


def menu(user):
    print(f"Welcome {user.user_name}!")
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
            user.history.append('You have listed all available items')

        elif user_choice == '2':
            search.search_for_item(user)

        elif user_choice == '3':
            search.search_by_category(user)

        elif user_choice == '4':
            print('Your history of search: ')
            user.print_history()
            print(f"Thank you for your visiting {user.user_name}")
            break

        else:
            print("You can chose only 1 - 3 for now\n")


if __name__ == '__main__':
    start()
