class Warehouse:

    def __init__(self,name, items) -> None:
        self.name = name
        self.items = items

    def print_items(self):

        print(f'\n{self.name}\n')

        for first, second, third in zip(self.items[::3], self.items[1::3], self.items[2::3]):
            print(f'{first:30}{second:30}{third:30}')

    def search_for_item(self, searched_item):
        return self.items.count(searched_item.capitalize())

    def search_after_letters(self, searched_letters):
        return {i for i in self.items if searched_letters.lower() in i.lower()}
