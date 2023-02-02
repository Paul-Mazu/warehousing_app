from datetime import datetime


class Item:

    def __init__(self, state: str, category: str, warehouse: int, date_of_stock: datetime) -> None:
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock

    def __str__(self):
        return f'{self.state} {self.category}'
