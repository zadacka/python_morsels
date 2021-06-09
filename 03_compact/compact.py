from collections import Collection, Counter
from itertools import chain, groupby


def compact_using_counter(input_iterable):
    return Counter(input_iterable).keys()


def compact_manual_approach(input_value):
    input_iterable = iter(input_value)
    try:
        current = next(input_iterable)
    except StopIteration:
        return input_iterable

    for element in input_iterable:
        if current != element:
            yield current
        current = element

    yield element


def compact_my_approach(input_value):
    """
    Not quite the neatest approach, but I'm including it because I came up with it myself
    """
    iterable = iter(input_value)

    a = object
    while iterable:
        b = next(iterable)
        if a != b:
            yield b
        a = b


def compact_neater(iterable):
    """
    From the solutions
    Using the same approach that I puzzled out, the form is simpler and more readable
    * no need to explicitly call iter()
    * no use of while, but rather uses clearer for x in y syntax
    * better naming!
    """
    previous = object  # object is unique so will never match an item in the iterator
    for item in iterable:
        if item != previous:
            yield item
        previous = item


def compact(iterable):
    """
    Also from the solutions ... and what I consider to be the best approach
    That which can be done by the standard library, should be...
    """
    return (item for item, group in groupby(iterable))
