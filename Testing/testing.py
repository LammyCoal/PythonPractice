import unittest
from Testing import testFuncts


class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        text = 'olleH'
        self.assertEqual(testFuncts.reverse_string("Hello"), text)

    def test_capitalize_string(self):
        text = 'Lammy'
        self.assertEqual(testFuncts.capitalize_string("lammy"), text)

    def test_is_capitalized(self):
        self.assertTrue(testFuncts.is_capitalized("Lammy"))
        self.assertFalse(testFuncts.is_capitalized("lammy"))


import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(get_sqrt(144), 12)
        with self.assertRaises(ValueError):
            get_sqrt(-144)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)


if __name__ == '__main__':
    unittest.main()