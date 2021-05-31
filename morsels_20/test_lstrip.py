import unittest

from morsels_20.lstrip import lstrip


class LStripTests(unittest.TestCase):

    """Tests for lstrip."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_list(self):
        self.assertIterableEqual(lstrip([1, 1, 2, 3, 1], 1), [2, 3, 1])

    def test_nothing_to_strip(self):
        self.assertIterableEqual(lstrip([1, 2, 3], 0), [1, 2, 3])

    def test_string(self):
        self.assertIterableEqual(lstrip('  hello', ' '), 'hello')

    def test_empty_iterable(self):
        self.assertIterableEqual(lstrip([], 1), [])

    def test_strip_all(self):
        self.assertIterableEqual(lstrip([1, 1, 1], 1), [])

    def test_none_values(self):
        self.assertIterableEqual(lstrip([None, 1, 2, 3], 0), [None, 1, 2, 3])

    def test_iterator(self):
        squares = (n**2 for n in [0, 0, 1, 2, 3])
        self.assertIterableEqual(lstrip(squares, 0), [1, 4, 9])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_returns_iterator(self):
        stripped = lstrip((1, 2, 3), 1)
        self.assertEqual(iter(stripped), iter(stripped))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_function_given(self):
        numbers = [0, 2, 4, 1, 3, 5, 6]
        def is_even(n): return n % 2 == 0
        self.assertIterableEqual(lstrip(numbers, is_even), [1, 3, 5, 6])


if __name__ == "__main__":
    unittest.main(verbosity=2)