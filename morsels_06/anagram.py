import unicodedata

from collections import Counter
from string import punctuation, whitespace


def is_anagram_my_solution(first_string, second_string):
    def comparable(phrase):
        deletion_table = str.maketrans({k: None for k in (punctuation + whitespace)})
        lowered = phrase.lower()
        nfkd_form = unicodedata.normalize('NFKD', lowered)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        string_again = only_ascii.decode('utf-8')
        translated = string_again.translate(deletion_table)
        return sorted(translated)

    return comparable(first_string) == comparable(second_string)


def is_anagram(word1, word2):
    """
    Nice tricks:
    * NFKD normalization
    * use isalpha() instead of stripping whitespace and punctuation via a map
    * use of counter to get more meaningful form of word for comparison
    * use of generator inside of the join()
    """
    def count_letters(word):
        normalized = unicodedata.normalize('NFKD', word)
        lowered = normalized.lower()
        alpha_only = ''.join(c for c in lowered if c.isalpha())
        return Counter(alpha_only)

    return count_letters(word1) == count_letters(word2)