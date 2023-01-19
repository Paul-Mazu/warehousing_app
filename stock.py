from collections import Counter
from sample.data import stock


def print_items():
    items_list = sorted([': '.join((diction['category'], diction['state'])) for diction in stock])
    counted_v = Counter(items_list)

    for k, v in counted_v.items():
        print(f'{k:35} {v:3} ea')

    print()
# triggers Counter() on list comprehension the result is object of Counter
    warehouses = Counter(dic['warehouse'] for dic in stock)
    for k, v in warehouses.items():
        print(f'Warehouse {k}: {v:4} items')

    # for first, second, third in zip(items_list[::3], items_list[1::3], items_list[2::3]):
    #     print(f'{first:30}{second:30}{third:30}')


def amount_items_on_stock(item: str):
    return [dic for dic in stock if ' '.join((dic['state'], dic['category'])).lower() == item.lower()]


def search_after_letter(letters):
    a_set = set([' '.join((diction['state'], diction['category'])) for diction in stock])
    new_list = []
    for i in a_set:
        if letters.lower() in i.lower(): new_list.append(i)
    return sorted(new_list)


def list_categories():
    return Counter(dc['category'] for dc in stock)
