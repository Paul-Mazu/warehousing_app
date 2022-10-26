from itertools import count
from data import warehouse1, warehouse2

user_name = input("What is your user name?: ")

print(f"Hello {user_name}!")

while True:

    user_choice = int(input(
        "What would you like to do?\n1. List items by warehouse\n2. Search an item and place an order\n3. Quit\nType the number of the operation: "))

    if user_choice == 1:

        print(warehouse1, "\n")
        print(warehouse2, "\n")
        
    elif user_choice == 2:
        item_to_search = input("What is the name of the item? ")

        available_items_in_warehouse1 = warehouse1.count(item_to_search)
        available_items_in_warehouse2 = warehouse2.count(item_to_search)
        available_items = {"warehouse1": available_items_in_warehouse1,
                        "warehouse2": available_items_in_warehouse2}
        print(f"Amount available: {sum(available_items.values())}")

        if sum(available_items.values()) > 0:

            max_avaiability = max(available_items.values())
            max_avaiability_in_which_warehouse = list(available_items.keys())[list(
                available_items.values()).index(max(available_items.values()))]

            if available_items_in_warehouse1 > 0 and available_items_in_warehouse2 > 0:
                print("Location: Both warehouses")
                print(
                    f"Maximum availability: {max_avaiability} in {max_avaiability_in_which_warehouse}")

            elif available_items_in_warehouse1 > 0 or available_items_in_warehouse2 > 0:
                print(f"Location: {max_avaiability_in_which_warehouse}")

            ordering_decision = input("would you like to order this item? (y/n): ")

            if ordering_decision == "y":

                number_of_items_to_order = int(input(
                    "How many item would you like to order?: "))

                if number_of_items_to_order <= sum(available_items.values()) and number_of_items_to_order > 0:
                    print(f"{number_of_items_to_order} {item_to_search} have been ordered")
                elif number_of_items_to_order > sum(available_items.values()):
                    buy_maximum = input(f"There is only {sum(available_items.values())} available. Would you like to order the maximum available? (y/n): ")
                    if buy_maximum == "y":
                        print(f"{sum(available_items.values())} {item_to_search} have been ordered")
                    else: print(f"Thank you for your visiting {user_name}")
                else: print("You have chosen wrong number")
            else: print(f"Thank you for your visiting {user_name}")

        else:
            check_another_item = input(f"This item is unaviable, do you want to check another item {user_name}? (y/n)")
            if check_another_item == n:
                break
    elif user_choice == 3:
        print(f"Thank you for your visiting {user_name}")
        break
