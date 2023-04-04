from classes import Employee

def test_if_is_authenticated():
    emp = Employee('Pawel', '1123')
    assert emp.is_authenticated

def test_authenticate():
    emp = Employee('Pawel', '1123')
    assert emp.authenticate('1123')
    assert not emp.authenticate('xxx')

def test_head_of_is_list():
    emp = Employee('Pawel', '1123')
    assert emp.head_of == []

def test_head_of_is_list():
    emp1 = Employee('XXX', 'abc')
    emp = Employee('Pawel', '1123', [emp1])
    assert len(emp.head_of) == 1