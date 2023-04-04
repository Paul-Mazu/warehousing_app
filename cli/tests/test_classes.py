import pytest

def test_bla_class_exists():
    try:
        from classes import Bla
    except ImportError:
        pytest.fail('Bla not found')

    assert hasattr(Bla, '__init__')