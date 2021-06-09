from timeit import default_timer
import unittest

from morsels_18.uniques import uniques_only


class UniquesOnlyTests(unittest.TestCase):

    """Tests for uniques_only."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_no_duplicates(self):
        self.assertIterableEqual(uniques_only([1, 2, 3]), [1, 2, 3])

    def test_adjacent_duplicates(self):
        self.assertIterableEqual(uniques_only([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_non_adjacent_duplicates(self):
        self.assertIterableEqual(uniques_only([1, 2, 3, 1, 2]), [1, 2, 3])

    def test_lots_of_duplicates(self):
        self.assertIterableEqual(uniques_only([1, 2, 2, 1, 1, 2, 1]), [1, 2])

    def test_accepts_iterator(self):
        nums = (n**2 for n in [1, 2, 3])
        self.assertIterableEqual(uniques_only(nums), [1, 4, 9])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_returns_iterator(self):
        nums = iter([1, 2, 3])
        output = uniques_only(nums)
        self.assertEqual(iter(output), iter(output))
        self.assertEqual(next(output), 1)
        # The below line tests that the incoming generator isn't exhausted.
        # It may look odd to test the squares input, but this is correct
        # because after 1 item has been consumed from the uniques_only
        # iterator, nums should only have 1 item consumed as well
        try:
            self.assertEqual(next(nums), 2)
        except StopIteration:
            self.fail("The incoming squares iterator was fully consumed!")

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_accepts_nonhashable_types(self):
        output = uniques_only([[1, 2], [3], [1], [3]])
        self.assertIterableEqual(output, [[1, 2], [3], [1]])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_hashable_types_faster(self):
        hashables = [(n, n+1) for n in range(1000)] + [0]
        unhashables = [[n] for n in range(1000)] + [0]
        with Timer() as hashable:
            for _ in uniques_only(hashables):
                pass
        with Timer() as unhashable:
            for _ in uniques_only(unhashables):
                pass
        self.assertLess(hashable.elapsed * 5, unhashable.elapsed)


class Timer:

    """Context manager to time a code block."""

    def __enter__(self):
        self.start = default_timer()
        return self

    def __exit__(self, *args):
        self.end = default_timer()
        self.elapsed = self.end - self.start


if __name__ == "__main__":
    unittest.main(verbosity=2)