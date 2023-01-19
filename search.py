import order
import stock
from datetime import datetime


def search_for_item(user, searched_item=None):
    if not searched_item:
        searched_item = input("Write the name of the searched item? ")

    while searched_item:

        available_items_list = stock.amount_items_on_stock(searched_item)
        sum_of_av_items = len(available_items_list)

        if sum_of_av_items > 0:
            print(f"Amount available: {sum_of_av_items} ea")

            for dc in available_items_list:
                time_delta = (datetime.now() - datetime.fromisoformat(dc["date_of_stock"])).days
                print(f'Warehouse {dc["warehouse"]} (in stock for {time_delta} days)')

            choice = input('Would you like to order this item? y/n: ')
            if choice == 'y':
                if not user.allowed:
                    print('You have to be signed in to order')
                else:
                    order.order_item(searched_item, sum_of_av_items)
            break

        else:
            print('There are such items found')
            searched_item = check_possible(searched_item)


def check_possible(searched_item):
    res_tuple = sorted(stock.search_after_letter(searched_item))

    if len(res_tuple) > 0:
        print('0. Exit')
        for num, i in enumerate(res_tuple, start=1):
            print(f'{num}. {i}')
        pick_item = input(f'Choose number 1 - {len(res_tuple)} to pick item or 0 to exit: ')

        if pick_item != '0':
            print(f'You have chosen {res_tuple[int(pick_item) - 1]}')
            return res_tuple[int(pick_item) - 1]
    else:
        print('Item not found')


def search_by_category():
    categories = stock.list_categories()
    a_list = []
    for n, (k, v) in enumerate(categories.items()):
        print(f'{n}. {k:12} {v}')
        a_list.append(k)
    choice = int(input('Pick the number to choose category: '))
    search_for_item(a_list[choice])


def search_again():
    answer = input('Would you like to search another item? (y/n): ')
    if answer != 'y':
        return None
