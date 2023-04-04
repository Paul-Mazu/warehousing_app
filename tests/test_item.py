from cli.classes import Item

def test_item():
    it = {"state": "High quality", "category": "USB hub", "warehouse": 1, "date_of_stock": "2020-08-01 02:58:45"}
    item = Item(**it)
    assert item.state == "High quality"
    assert item.category == "USB hub"
    assert item.date_of_stock == "2020-08-01 02:58:45"
    assert item.__str__() == "High quality USB hub"