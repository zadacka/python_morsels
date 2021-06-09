from operator import itemgetter
import unittest

from group_by import group_by


class GroupByTests(unittest.TestCase):

    """Tests for group_by."""

    def test_test_tuples_of_strings(self):
        animals = [
            ('agatha', 'dog'),
            ('kurt', 'cat'),
            ('margaret', 'mouse'),
            ('cory', 'cat'),
            ('mary', 'mouse'),
        ]
        animals_by_type = {
            'mouse': [('margaret', 'mouse'), ('mary', 'mouse')],
            'dog': [('agatha', 'dog')],
            'cat': [('kurt', 'cat'), ('cory', 'cat')],
        }
        output = group_by(animals, key_func=itemgetter(1))
        self.assertEqual(output, animals_by_type)

    def test_strings(self):
        words = ["Apple", "animal", "apple", "ANIMAL", "animal"]
        word_groups = {
            "apple": ["Apple", "apple"],
            "animal": ["animal", "ANIMAL", "animal"],
        }
        output = group_by(words, key_func=str.lower)
        self.assertEqual(output, word_groups)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_no_key_function(self):
        words = ["apple", "animal", "apple", "animal", "animal"]
        word_groups = {
            "apple": ["apple", "apple"],
            "animal": ["animal", "animal", "animal"],
        }
        output = group_by(words)
        self.assertEqual(output, word_groups)


if __name__ == "__main__":
    unittest.main()