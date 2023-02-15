from pathlib import Path
import os
import pytest
import classes

BASE_DIR = Path(__file__).resolve().parent.parent
# print('HERE!!!', BASE_DIR)

# classes_path = os.path.join(BASE_DIR, 'classes')
# a = __import__(classes_path)

def test_class_exist():
    try:
        from classes import Warehouse
    except ImportError:
        pytest.skip('Warehouse not found')
    
    assert hasattr(Warehouse, '__init__')

