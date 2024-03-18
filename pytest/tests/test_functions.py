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
    assert result == 6

def test_add_strings():
    result = add_numbers("Shahmeer", " Khan")
    assert result == "Shahmeer Khan"

def test_divide():
    result = divide_numbers(10,2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10,0)