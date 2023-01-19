def order_item(user, item, sum_of_available_items):
    correct_order = False
    while not correct_order:

        number_of_items_to_order = int(input("How many items would you like to order?: "))

        if sum_of_available_items >= number_of_items_to_order > 0:
            print(f"{number_of_items_to_order} of {item} have been ordered, thank you")
            user.history.append(f'You have ordered {number_of_items_to_order} of {item}')
            correct_order = True

        elif number_of_items_to_order < 1:
            print("The number of items is incorrect")
            if input("Do you still want to order the item? (y/n)") == "n":
                print('Thank you')
                correct_order = True

        else:
            print(f"There is only {sum_of_available_items} items available")
            answer = int(order_max_or_not())

            if answer == 1:
                print(f"{sum_of_available_items} of {item} have been ordered")
                user.history.append(f'You have ordered {sum_of_available_items} of {item}')
                correct_order = True

            elif answer == 2:
                print(f'You can order maximally {sum_of_available_items} items')

            elif answer == 3:
                break


def order_max_or_not():
    while True:
        choice = input('Would you like to order:\n'
                       '1. maximum items\n'
                       '2. different number of items\n'
                       '3. go back to menu\n')
        if choice in ('1', '2', '3'):
            return choice
        else:
            print("Answer unknown, these are possible answers: ")
