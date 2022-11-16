import search

def if_order(item, sum, stock):
    choice = input('Would you like to order this item? y/n: ')
    if choice == 'y':
        order_item(item, sum)
    else:
        choice1 = input('Would you like to check another item? y/n: ')
        if choice1 == 'y':
            search.search_for_item(stock)

def order_item(item, sum_of_available_items):
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
