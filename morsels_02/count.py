from collections import Counter

import re


def count_words_attempt(text):
    # from string import punctuation
    # text.replace(punctuation, '')
    # you might think that this would replace any of the characters in punctuation
    # but you'd be wrong for two reasons:
    # 1. you are confusing replace (which does whole sub-strings) with translate
    # 2. and the signature of translate has changed in Python 3 to use tables...
    words = text.split()
    sorted_lowered_words = sorted([w.lower() for w in words])
    return Counter(sorted_lowered_words)


def count_words(text):
    """ not wild about the use of regex, but it is difficult to
      achieve the kind of 'ignore punctuation except inside words'
      precision required by outright replacing/stripping punctuation """
    return Counter(re.findall(r"\b[\w'-]+\b", text.lower()))
