# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

from anagram import is_anagram


class IsAnagramTests(unittest.TestCase):

    """Tests for is_anagram."""

    def test_short_anagram(self):
        self.assertTrue(is_anagram("tea", "eat"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("tea", "treat"))

    def test_sink_and_skin(self):
        self.assertTrue(is_anagram("sink", "skin"))

    def test_same_letters_different_lengths(self):
        self.assertFalse(is_anagram("sinks", "skin"))

    def test_different_capitalization(self):
        self.assertTrue(is_anagram("Trey", "Yert"))
        self.assertTrue(is_anagram("Listen", "silent"))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_spaces_ignored(self):
        phrase1 = "William Shakespeare"
        phrase2 = "I am a weakish speller"
        self.assertTrue(is_anagram(phrase1, phrase2))
        self.assertFalse(is_anagram("a b c", "a b d"))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_punctation_ignored(self):
        phrase1 = "A diet"
        phrase2 = "I'd eat"
        self.assertTrue(is_anagram(phrase1, phrase2))

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_characters_with_accents(self):
        self.assertTrue(is_anagram("Siobhán Donaghy", "Shanghai Nobody"))


if __name__ == "__main__":
    unittest.main()