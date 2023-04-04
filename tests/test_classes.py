def test_warehouse_class_exists():

    from classes import Warehouse
    assert hasattr(Warehouse, '__init__')

def test_item_class_exists():
    from classes import Item
    assert hasattr(Item, '__init__')

def test_user_class_exists():
    from classes import User
    assert hasattr(User, '__init__')

def test_employee_class_exists():
    from classes import Employee
    assert hasattr(Employee, '__init__')

def test_employee_is_user():
    from classes import Employee
    from classes import User
    employee = Employee('Pawel', '1234')
    assert isinstance(employee, User)

def test_employee_is_user_to_fail():
    from classes import Employee
    from classes import Item
    employee = Employee('Pawel', '1234')
    assert not isinstance(employee, Item)

