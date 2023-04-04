from cli.classes import Warehouse, Item

def test_warehouse_id():
    wh = Warehouse(1)
    assert wh.warehouse_id == 1
    assert wh.stock == []
    assert wh.occupancy() == 0
    item = Item('','','','')
    wh.add_item(item)
    assert wh.occupancy() == 1
    