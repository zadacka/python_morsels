import unittest


from tail import tail


class TailTests(unittest.TestCase):

    """Tests for tail."""

    def test_zero(self):
        self.assertEqual(tail([1, 2], 0), [])

    def test_one(self):
        self.assertEqual(tail([1, 2], 1), [2])

    def test_two(self):
        self.assertEqual(tail([1, 2], 2), [1, 2])

    def test_n_larger_than_iterable_length(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(tail(nums, 5), [1, 2, 3, 4])
        self.assertEqual(tail([], 10), [])

    def test_string(self):
        self.assertEqual(tail('hello', 2), ['l', 'o'])

    def test_tuple(self):
        self.assertEqual(tail((1, 2, 3), 3), [1, 2, 3])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_negative_n(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(tail(nums, -1), [])
        self.assertEqual(tail((), -9), [])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_iterator(self):
        nums = (n**2 for n in [1, 2, 3, 4])
        self.assertEqual(tail(nums, -1), [])
        self.assertEqual(tail(nums, 2), [9, 16])
        self.assertEqual(tail(nums, 0), [])
        self.assertEqual(tail(nums, 1), [])


if __name__ == "__main__":
    unittest.main()