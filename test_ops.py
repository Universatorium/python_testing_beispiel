from ops import *

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10,5) == 2

import unittest

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

class TestDivideFunction(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
