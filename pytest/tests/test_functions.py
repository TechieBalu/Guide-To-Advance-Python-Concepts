from icecream import ic
import pathlib
import sys
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ic(BASE_DIR)
sys.path.append(str(BASE_DIR))
ic(sys.path)
import pytest
from functions.functions_file import add_numbers, divide_numbers




def test_add():
    result = add_numbers(1, 5)
    assert result == 7

def test_divide():
    result = divide_numbers(10,2)
    assert result == 5
