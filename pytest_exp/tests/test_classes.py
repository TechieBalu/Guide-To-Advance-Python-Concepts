import pathlib
import sys
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
from classes.shapes import Shape


class TestCirlce:

    def test_one(self):
        assert True