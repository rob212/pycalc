import unittest
from calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(calculate(1, 2), "sum is 3")
