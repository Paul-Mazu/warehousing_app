from itertools import count
from data import warehouse1, warehouse2

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
        choice = int(input("Would you like to order:\n1. maximum items\n2. different number of items\n3. check another item\n4. return to menu:\n"))
        if choice in range(1, 5):
            return choice
        else: print("Answer unknown, these are possible answers: ")

def want_check_another_item():
    check_other_item = input(f"Would you like to check another item {user_name}? (y/n): ")
    if check_other_item == "n":
        return "n"

def ordering_logic():
    
    back_to_menu = False
    while back_to_menu == False:
        
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
                
                correct_order = False

                while correct_order == False:
                    number_of_items_to_order = int(
                        input("How many items would you like to order?: "))

                    if number_of_items_to_order <= sum_of_available_items and number_of_items_to_order > 0:
                        print(f"{number_of_items_to_order} of {item_to_search} have been ordered")
                        correct_order = True
                        
                    elif number_of_items_to_order > sum_of_available_items:
                        print(f"There is only {sum_of_available_items} items available")
                        answer = order_max_or_not()
                        quick_back_to_menu = False #quick go to menu
                        quick_check_another_item = False
                        
                        if answer == 1:
                            print(f"{sum_of_available_items} of {item_to_search} have been ordered")
                            correct_order = True
                            
                        elif answer == 2:
                            while True:
                                how_much_to_order = int(input("How much to order?: "))
                                
                                if how_much_to_order > 0 and how_much_to_order <= sum_of_available_items:
                                    print(f"{how_much_to_order} {item_to_search} have been ordered")
                                    correct_order = True
                                    break
                                
                                elif how_much_to_order <= 0:
                                    print("The number of items is incorect")
                                    if input("Do you still want to order the item? (y/n)") == "n":
                                        break  
                                    
                                else: print("You have to choose available amount")
                        elif answer == 3:
                            correct_order = True
                            quick_check_another_item = True
                        
                        elif answer == 4:
                            correct_order = True
                            quick_back_to_menu = True
                                
                    else: 
                        print("The number of items is incorect")
                        if input("Do you still want to order the item? (y/n)") == "n":
                            correct_order = True   
                                             
                if quick_back_to_menu == False:
                    if quick_check_another_item == False:
                        if want_check_another_item() == "n":
                            back_to_menu = True
                else: back_to_menu = True
                    
            else:
                if want_check_another_item() == "n":
                    back_to_menu = True
        else:
            print("This item is unavailable")
            if want_check_another_item() == "n":
                back_to_menu = True


start()
