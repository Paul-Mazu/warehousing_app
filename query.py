from itertools import count
from unicodedata import name
from data import warehouse1, warehouse2
from tk import *

user_name = input("What is your user name?: ")


def start():
    print(f"Hello {user_name}!")    
    menu()


def menu():
    while True:
        user_choice = int(input(
            "\nWhat would you like to do?\n1. List items by warehouse\n2. Search an item and place an order\n3. Quit\nType the number of the operation: "))
        if user_choice == 1:
            printing_warehouses()

        elif user_choice == 2:
            ordering_logic()

        elif user_choice == 3:
            print(f"Thank you for your visiting {user_name}")
            break

        else:
            print("You can chose only 1 - 3 for now\n")
            


def printing_warehouses():
    print(warehouse1, "\n")
    print(warehouse2, "\n")

def searching_engine(item):
    available_items_in_warehouse1 = warehouse1.count(item)
    available_items_in_warehouse2 = warehouse2.count(item)
    available_items_dictionary = {"warehouse1": available_items_in_warehouse1,
                                      "warehouse2": available_items_in_warehouse2}
    return available_items_dictionary

def order_max_or_not():
    while True:
        choice = int(input("Would you like to order:\n1. maximum items\n2.different number of items\n3. check another item\n4.return to menu "))
        if choice in range(1, 5):
            return choice
        else: print("Answer unknown, these are possible answers: ")

def ordering_logic():
    while True:
        
        item_to_search = input("What is the name of the item? ")
        
        available_items_dict = searching_engine(item_to_search)
        sum_of_available_items = sum(available_items_dict.values())

        if sum_of_available_items > 0:

            print(f"Amount available: {sum_of_available_items}")
            
            for k, v in available_items_dict.items():
                print(f"In {k} available is: {v} items")

            ordering_decision = input(
                "Would you like to order this item? (y/n): ")

            if ordering_decision == "y":

                number_of_items_to_order = int(
                    input("How many items would you like to order?: "))

                if number_of_items_to_order <= sum_of_available_items and number_of_items_to_order > 0:
                    print(f"{number_of_items_to_order} of {item_to_search} have been ordered")
                    
                elif number_of_items_to_order > sum_of_available_items:
                    print(f"There is only {sum_of_available_items} items available")
                    answer = order_max_or_not()
                    
                    if answer == 1:
                        print(f"{sum_of_available_items} of {item_to_search} have been ordered")
                        
                    elif answer ==2:
                        while True:
                            how_much_to_order = int(input("How much to order?: "))
                            if how_much_to_order > 0 and how_much_to_order < sum_of_available_items:
                                print(f"{how_much_to_order} {item_to_search} have been ordered")
                                break
                            elif how_much_to_order <= 0:
                                print("Order wasn't placed")
                                break
                            else: print("You have to choose available amount")
                        
            else:
                check_other_item = input(
                    f"Would you like to check another item {user_name}? (y/n): ")
            if check_other_item == "n":
                break
        else:
            check_another_item = input(
                f"This item is unaviable, do you want to check another item {user_name}? (y/n)")
            if check_another_item == "n":
                break


start()
