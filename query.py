import pprint

from data import warehouse1, warehouse2

while True:
    user_name = input("What is your user name?: ")
    if len(user_name):
        break
    else:
        print('Please input your user name')


def start():
    print(f"Hello {user_name}!")
    menu()


def menu():
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
            ordering_logic()

        elif user_choice == '3':
            print(f"Thank you for your visiting {user_name}")
            break

        else:
            print("You can chose only 1 - 3 for now\n")


def printing_warehouses():
    print('\nWarehouse 1:\n')
    for first, second, third in zip(warehouse1[::3], warehouse1[1::3], warehouse1[2::3]):
        print(f'{first:30}{second:30}{third:30}')

    print('\nWarehouse 2:\n')
    for first, second, third in zip(warehouse2[::3], warehouse2[1::3], warehouse2[2::3]):
        print(f'{first:30}{second:30}{third:30}')


def searching_logic(item):
    while True:
        available_items_in_warehouse1 = warehouse1.count(item.capitalize())
        available_items_in_warehouse2 = warehouse2.count(item.capitalize())
        available_items_dictionary = {"warehouse1": available_items_in_warehouse1,
                                      "warehouse2": available_items_in_warehouse2}
        suma = available_items_in_warehouse1 + available_items_in_warehouse2
        if suma > 0:
            return available_items_dictionary
        else:
            wh_set = {i for i in warehouse1 if item.lower() in i.lower()} | {i for i in warehouse2 if item.lower() in i.lower()}
            wh_tuple = tuple(wh_set)
            if len(wh_set) > 0:
                print('We did not find the item, did you mean?: ')
                print('0. Go back')
                counter = 0
                for i in wh_set:
                    counter += 1
                    print(f'{counter}. {i}')

                item_pick_from_number = input('Choose number or "0" to return to search: ')
                if int(item_pick_from_number) == 0:
                    return {}
                elif int(item_pick_from_number) in range(len(wh_tuple)):
                    item = wh_tuple[int(item_pick_from_number)-1]
            else:
                return {}


def order_max_or_not():
    while True:
        choice = input('Would you like to order:\n'
                       '1. maximum items\n'
                       '2. different number of items\n'
                       '3. check another item\n'
                       '4. return to menu:\n')
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Answer unknown, these are possible answers: ")


def want_check_another_item():
    check_other_item = input(f'Would you like to check another item {user_name}? (y/n): ')
    if check_other_item == "n":
        return "n"


def ordering_logic():
    back_to_menu = False
    while not back_to_menu:

        item_to_search = input("What is the name of the item? ")
        available_items_dict = searching_logic(item_to_search)
        sum_of_available_items = sum(available_items_dict.values())

        if sum_of_available_items > 0:

            print(f"Amount available: {sum_of_available_items}")

            for k, v in available_items_dict.items():
                print(f'In {k} available is: {v} items')

            ordering_decision = input(
                "Would you like to order this item? (y/n): ")

            if ordering_decision == 'y':
                check_another = ordering_items(item_to_search, sum_of_available_items)
                if check_another == 'check another':
                    continue
                elif check_another:
                    back_to_menu = True
                elif want_check_another_item() == 'n':
                    back_to_menu = True

            else:
                if want_check_another_item() == 'n':
                    back_to_menu = True
        else:
            print("This item is unavailable")
            if want_check_another_item() == 'n':
                back_to_menu = True


def ordering_items(item, sum_of_available_items):
    correct_order = False
    while not correct_order:

        number_of_items_to_order = int(input("How many items would you like to order?: "))

        if sum_of_available_items >= number_of_items_to_order > 0:
            print(f"{number_of_items_to_order} of {item} have been ordered")
            correct_order = True

        elif number_of_items_to_order < 1:
            print("The number of items is incorrect")
            if input("Do you still want to order the item? (y/n)") == "n":
                correct_order = True

        else:
            print(f"There is only {sum_of_available_items} items available")
            answer = order_max_or_not()

            if answer == 1:
                print(f"{sum_of_available_items} of {item} have been ordered")
                correct_order = True

            elif answer == 2:
                print(f'You can order maximally {sum_of_available_items} items')

            elif answer == 3:
                return 'check another'

            elif answer == 4:
                return True


start()
