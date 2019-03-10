from collections import deque


def tail_simple(sequence, index):
    if index <= 0:
        return []
    return list(sequence[-index:])


def tail_walk_the_iterable(sequence, n):
    """
    Motivation: if we're handling a generator it may be desirable *not*
    to load everything into memory. This approach walks through and only
    holds the necessary elements in memory.
    """
    if n <= 0:
        return []

    index = slice(0, 0) if n == 1 else slice(-n + 1, None)

    result = []
    for element in sequence:
            result = [*result[index], element]
    return result


def tail(sequence, n):
    """
    As usual, there's a nice standard library thing that will do exactly what
    we want. Specifically, the 'double ended queue' type that can have a
    maxlength and be initialised from another iterable. And voila, we're done.
    """
    if n <= 0:
        return []
    return list(deque(sequence, maxlen=n))
