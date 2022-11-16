from data import warehouse1, warehouse2

def printing_warehouses():
    print('\nWarehouse 1:\n')
    for first, second, third in zip(warehouse1[::3], warehouse1[1::3], warehouse1[2::3]):
        print(f'{first:30}{second:30}{third:30}')

    print('\nWarehouse 2:\n')
    for first, second, third in zip(warehouse2[::3], warehouse2[1::3], warehouse2[2::3]):
        print(f'{first:30}{second:30}{third:30}')