from classes import User

def test_user_no_argument():
    user = User()
    assert user._name == 'Guest'

def test_user_with_argument():
    user = User('Pawel')
    assert user._name == 'Pawel'

def test_user_is_authenticated():
    user = User()
    assert user.is_authenticated == False
    assert not user.authenticate('1111')