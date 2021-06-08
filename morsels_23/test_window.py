import unittest

from window import window


class WindowTests(unittest.TestCase):

    """Tests for window."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_window_size_2(self):
        inputs = [1, 2, 3]
        outputs = [(1, 2), (2, 3)]
        self.assertIterableEqual(window(inputs, 2), outputs)

    def test_window_size_1(self):
        self.assertIterableEqual(window([1, 2, 3], 1), [(1,), (2,), (3,)])
        self.assertIterableEqual(window([1], 1), [(1,)])

    def test_none(self):
        inputs = [None, None]
        outputs = [(None, None)]
        self.assertIterableEqual(window(inputs, 2), outputs)

    def test_string(self):
        inputs = "hey"
        outputs = [('h', 'e'), ('e', 'y')]
        self.assertIterableEqual(window(inputs, 2), outputs)

    def test_window_size_3(self):
        inputs = [1, 2, 3, 4, 5, 6]
        outputs = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
        self.assertIterableEqual(window(inputs, 3), outputs)

    def test_window_size_4(self):
        inputs = [1, 2, 3, 4, 5, 6]
        outputs = [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]
        self.assertIterableEqual(window(inputs, 4), outputs)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_accepts_iterator(self):
        inputs = (n**2 for n in [1, 2, 3, 4])
        outputs = [(1, 4), (4, 9), (9, 16)]
        self.assertIterableEqual(window(inputs, 2), outputs)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_returns_lazy_iterable(self):
        inputs = (n**2 for n in [1, 2, 3, 4, 5])
        iterable = window(inputs, 2)
        self.assertEqual(iter(iterable), iter(iterable))
        self.assertEqual(next(iterable), (1, 4))
        self.assertEqual(next(inputs), 9)
        self.assertEqual(list(iterable), [(4, 16), (16, 25)])


if __name__ == "__main__":
    unittest.main(verbosity=2)