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
        return [item for item in self.stock if searched_item.lower() == item.__str__().lower()]

    def print_items(self):
        print(f'Warehouse: {self.warehouse_id}')
        for k, v in self.count_same_items().items():
            print(f'{k:33}: {v:2}')

    def count_same_items(self):
        dic = {}
        for item in self.stock:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        return dic


class Item:

    def __init__(self, state, category, warehouse, date_of_stock: datetime):
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock
        self.warehouse_id = warehouse

    def __str__(self):
        return f'{self.state} {self.category}'

    def __eq__(self, other):
        if self.state == other.state and self.category == other.category:
            return True
        return False

    def __hash__(self):
        return hash(self.state + self.category)

    def __format__(self, format_spec):
        return f"{self.__str__():{format_spec}}"


class User:
    def __init__(self, user_name='Guest'):
        self._name = user_name
        self.is_authenticated = False

    def authenticate(self, password):
        return False

    def is_named(self, name):
        if self._name == name:
            return True
        return False

    def greet(self):
        print(f'''Hello, {self._name}!
Welcome to our Warehouse Database.
If you don't find what you are looking for,
please ask one of our staff members to assist you.''')

    def bye(self):
        print('Thank you fir visiting', self._name)

    def get_name(self):
        return self._name


class Employee(User):
    def __init__(self, user_name, password, head_of=None):
        super(Employee, self).__init__(user_name)
        if head_of is None:
            head_of = []
        self.__password = password
        self.head_of = head_of
        self.is_authenticated = True
        self.history = []

    def __str__(self):
        return f'{self.get_name()} {self.__password}'

    def authenticate(self, password):
        if password == self.__password:
            return True
        return False

    def order(self, item: Item, amount: int):
        return f'{amount} of {item} was ordered!'

    def greet(self):
        print(f'''Hello, {self.get_name()}!
If you experience a problem with the system,
please contact technical support.''')

    def add_to_history(self, log):
        self.history.append(log)

    def print_history(self):
        for el in self.history:
            print(el)

