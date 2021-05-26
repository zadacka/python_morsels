import unittest

from morsels_19.interleave import interleave


class InterleaveTests(unittest.TestCase):

    """Tests for interleave."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_empty_lists(self):
        self.assertIterableEqual(interleave([], []), [])

    def test_single_item_each(self):
        self.assertIterableEqual(interleave([1], [2]), [1, 2])

    def test_two_items_each(self):
        self.assertIterableEqual(interleave([1, 2], [3, 4]), [1, 3, 2, 4])

    def test_four_items_each(self):
        in1 = [1, 2, 3, 4]
        in2 = [5, 6, 7, 8]
        out = [1, 5, 2, 6, 3, 7, 4, 8]
        self.assertIterableEqual(interleave(in1, in2), out)

    def test_none_value(self):
        in1 = [1, 2, 3, None]
        in2 = [4, 5, 6, 7]
        out = [1, 4, 2, 5, 3, 6, None, 7]
        self.assertIterableEqual(interleave(in1, in2), out)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_non_sequences(self):
        in1 = [1, 2, 3, 4]
        in2 = (n**2 for n in in1)
        out = [1, 1, 2, 4, 3, 9, 4, 16]
        self.assertIterableEqual(interleave(in1, in2), out)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_response_is_iterator(self):
        cubes = (n**3 for n in [1, 2, 3])
        squares = (n**2 for n in [4, 5, 6])
        output = interleave(cubes, squares)
        self.assertIs(iter(output), iter(output))
        self.assertEqual(next(output), 1)
        self.assertEqual(next(output), 16)
        self.assertEqual(next(output), 8)
        # The below line tests that the incoming generator isn't exhausted.
        # It may look odd to test the squares input, but this is correct
        # because after 2 items have been consumed from the interleave output
        # iterator, squareus should only have 2 items consumed
        try:
            self.assertEqual(next(cubes), 27)
        except StopIteration:
            self.fail("The incoming squares iterator was fully consumed!")


if __name__ == "__main__":
    unittest.main(verbosity=2)