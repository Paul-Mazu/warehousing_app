from data import warehouse2, warehouse1

### count inputed item in lists wh1 & wh2 and return dict
### if 0 items found, check if phrase in items in lists, remove repetition and show choices
### chosen item count in lists wh1 & wh2

def searching_logic(item):

    while True:
        available_items_in_warehouse1 = warehouse1.count(item.capitalize())
        available_items_in_warehouse2 = warehouse2.count(item.capitalize())
        available_items_dictionary = {"warehouse1": available_items_in_warehouse1,
                                      "warehouse2": available_items_in_warehouse2}
        sum_of_av_items = available_items_in_warehouse1 + available_items_in_warehouse2

        if sum_of_av_items > 0:
            return available_items_dictionary
        else:
            wh1_set = {i for i in warehouse1 if item.lower() in i.lower()}
            wh2_set = {i for i in warehouse2 if item.lower() in i.lower()}
            wh_sets =  wh1_set | wh2_set
            wh_tuple = sorted(tuple(wh_sets))

            if len(wh_tuple) > 0:
                print('We did not find the item, did you mean?: ')
                print('0. Go back')

                for num, i in enumerate(wh_tuple, start=1):
                    print(f'{num}. {i}')

                item_pick_from_number = input('Choose number or "0" to return to search: ')
                if int(item_pick_from_number) == 0:
                    return {}
                elif int(item_pick_from_number) in range(len(wh_tuple)+1):
                    item = wh_tuple[int(item_pick_from_number)-1]
                    print(f'You have chosen: {item}')

            else:
                return {}
