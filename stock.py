import warehouse as w
import data

class Stock:

    def __init__(self) -> None:
        wh1 = w.Warehouse('Warehouse 1', data.warehouse1) 
        wh2 = w.Warehouse('Warehouse 2', data.warehouse2)
        self.warehauses = [wh1, wh2]

    def add_warehouse(self, warehouse):
        self.warehauses.append(warehouse)
    
    def del_warehouse(self, warehouse):
        self.warehauses.remove(warehouse)

    def print_warehouses(self):
        for wh in self.warehauses:
            wh.print_items()

    def amount_items_on_stock(self, item):
        dic = {}
        for wh in self.warehauses:
            dic[wh.name] = wh.search_for_item(item)
        return dic

    def search_after_letter(self, letters):
        a_set = set()
        for wh in self.warehauses:
            a_set.update(wh.search_after_letters(letters))
        return tuple(a_set)