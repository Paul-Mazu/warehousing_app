import datetime


class Warehouse:

    def __init__(self, warehouse_id: int):
        self.warehouse_id = warehouse_id
        self.stock = []

    def occupancy(self):
        return len(self.stock)

    def add_item(self, item):
        self.stock.append(item)

    def search(self, searched_item: str):
        return [item for item in self.stock if searched_item.lower() in item.__str__().lower()]

    def print_items(self):
        for el in self.stock:
            print(el)


class Item:

    def __init__(self, state, category, date_of_stock: datetime):
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock

    def __str__(self):
        return f'{self.state} {self.category}'


class User:
    def __init__(self, user_name='Anonymous'):
        self._name = user_name
        self.is_authenticated = False

    def authenticate(self):
        return False


class Employee:
