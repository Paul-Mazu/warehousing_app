def search_for_item(stock):

    searched_item = input("Write the name of the searched item? ")
    while searched_item:
        available_items_dic = stock.amount_items_on_stock(searched_item)
        sum_of_av_items = sum(available_items_dic.values())

        if sum_of_av_items > 0:
            print(f"Amount available: {sum_of_av_items} ea")

            for k, v in available_items_dic.items():
                print(f'In {k} is available {v} ea of {searched_item}')
            return (searched_item, sum_of_av_items)

        else:
            searched_item = check_possible(stock, searched_item)


def check_possible(stock, searched_item):
    res_tuple = sorted(stock.search_after_letter(searched_item))
    
    if len(res_tuple) > 0:
        print('There is no such item. Did you mean?: ')
        print('0. Go back')
        for num, i in enumerate(res_tuple, start=1):
            print(f'{num}. {i}')
        pick_item = input(f'Choose number 1 - {len(res_tuple)} to pick item or "0" to go back: ')
        
        print(f'You have chosen {res_tuple[int(pick_item)-1]}')

        return res_tuple[int(pick_item)-1]
    else: 
        print('Item not found')
        return None



