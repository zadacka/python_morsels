from decimal import Decimal
from datetime import timedelta
from fractions import Fraction
import unittest

from deep_add import deep_add


class DeepAddTests(unittest.TestCase):

    """Tests for deep_add."""

    def test_shallow(self):
        self.assertEqual(deep_add([1, 2, 3, 4]), 10)

    def test_with_empty_lists(self):
        self.assertEqual(deep_add([1, [2, 3, []], [], 4]), 10)
        self.assertEqual(deep_add([]), 0)

    def test_deeply_nested_iterables(self):
        self.assertEqual(deep_add([[1, 2], [3, [4, [[[5]], 6]]]]), 21)

    def test_non_numeric_types(self):
        with self.assertRaises(TypeError):
            deep_add([1, [2, None]])

    def test_other_numeric_types(self):
        self.assertEqual(deep_add([1.0, [3, 1.5]]), 5.5)
        self.assertEqual(deep_add([1.0, [3j]]), 1+3j)
        self.assertEqual(deep_add([Decimal('5.6'), 2]), Decimal('7.6'))
        self.assertEqual(deep_add([[Fraction(1)], Fraction(2)]), Fraction(3))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_other_iterables(self):
        numbers = [1, 2, 3, 4]
        cubes_and_squares = ((n, (n**3, n**2)) for n in numbers)
        self.assertEqual(deep_add(cubes_and_squares), 140)
        self.assertEqual(deep_add([(1, 2), [3, {4, 5}]]), 15)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_start_value(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(deep_add(numbers, 0), 10)
        self.assertEqual(deep_add(numbers, 1), 11)
        self.assertEqual(deep_add(numbers, start=1), 11)
        self.assertEqual(deep_add([[], []], start=-10), -10)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_pseudonumeric_types(self):
        self.assertEqual(deep_add([timedelta(1)], timedelta(0)), timedelta(1))
        class Num:
            def __init__(self, val=0):
                self.val = val
            def __add__(self, other):
                if isinstance(other, Num):
                    return Num(self.val + other.val)
                else:
                    return Num(self.val + other)
            __radd__ = __add__
            def __eq__(self, other):
                return self.val == other.val
        self.assertEqual(deep_add([[Num(1)], Num(2)]), Num(3))


if __name__ == "__main__":
    unittest.main()