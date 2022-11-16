import searching

### run search and receive back dictionary with items
### if values > 0 order -> go to fun: search, otherwise, ask if search again

def search_and_order():
    back_to_menu = False
    while not back_to_menu:

        item_to_search = input("What is the name of the item? ")
        available_items_dict = searching.searching_logic(item_to_search)
        sum_of_available_items = sum(available_items_dict.values())

        if sum_of_available_items > 0:

            print(f"Amount available: {sum_of_available_items}")

            for k, v in available_items_dict.items():
                print(f'In {k} available is: {v} items')

            ordering_decision = input(
                "Would you like to order this item? (y/n): ")

            if ordering_decision == 'y':
                check_another = search(item_to_search, sum_of_available_items)
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

def search(item, sum_of_available_items):
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
            answer = int(order_max_or_not())

            if answer == 1:
                print(f"{sum_of_available_items} of {item} have been ordered")
                correct_order = True

            elif answer == 2:
                print(f'You can order maximally {sum_of_available_items} items')

            elif answer == 3:
                return 'check another'

            elif answer == 4:
                return True


def order_max_or_not():
    while True:
        choice = input('Would you like to order:\n'
                       '1. maximum items\n'
                       '2. different number of items\n'
                       '3. check another item\n'
                       '4. return to menu:\n')
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Answer unknown, these are possible answers: ")


def want_check_another_item():
    check_other_item = input(f'Would you like to check another item? (y/n): ')
    if check_other_item == "n":
        return "n"