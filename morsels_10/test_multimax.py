import unittest

from multimax import multimax


class MultiMaxTests(unittest.TestCase):

    """Tests for multimax."""

    def test_single_max(self):
        self.assertEqual(multimax([1, 2, 4, 3]), [4])

    def test_two_max(self):
        self.assertEqual(multimax([1, 4, 2, 4, 3]), [4, 4])

    def test_all_max(self):
        self.assertEqual(multimax([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_lists(self):
        inputs = [[0], [1], [], [0, 1], [1]]
        expected = [[1], [1]]
        self.assertEqual(multimax(inputs), expected)

    def test_order_maintained(self):
        inputs = [
            (3, 2),
            (2, 1),
            (3, 2),
            (2, 0),
            (3, 2),
        ]
        expected = [
            inputs[0],
            inputs[2],
            inputs[4],
        ]
        outputs = multimax(inputs)
        self.assertEqual(outputs, expected)
        self.assertIs(outputs[0], expected[0])
        self.assertIs(outputs[1], expected[1])
        self.assertIs(outputs[2], expected[2])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_empty(self):
        self.assertEqual(multimax([]), [])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_iterator(self):
        numbers = [1, 4, 2, 4, 3]
        squares = (n**2 for n in numbers)
        self.assertEqual(multimax(squares), [16, 16])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_key_function(self):
        words = ["alligator", "animal", "apple", "artichoke", "avalanche"]
        outputs = ["alligator", "artichoke", "avalanche"]
        self.assertEqual(multimax(words, key=len), outputs)


if __name__ == "__main__":
    unittest.main()