def window_alex(content, n):
    from collections import deque
    result = deque()
    iterable = iter(content)
    for i in iterable:
        result.append(i)
        if len(result) < n:
            continue
        if len(result) > n:
            result.popleft()
        yield tuple(result)

    if len(result) < n:
        yield tuple()


def window_trey1(sequence, n):
    """Return list of tuples of items in given list and next n-1 items."""
    # really nice use of 'shortest' zip behaviour
    sequences = [sequence[i:] for i in range(n)]
    return zip(*sequences)


def window_trey_best(iterable, n):
    """
    use islice (nice!) to populate the first iterable,
    use maxlen so that you never have to popleft() from the deque
    """
    iterator = iter(iterable)
    from collections import deque
    from itertools import islice
    current = deque(islice(iterator, n), maxlen=n)
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)


def window(iterable, n):
    from itertools import islice
    from itertools import tee
    iterators = [
        islice(iterator, i, None)  # stop = 'None' ... continue until iterator is exhausted
        for i, iterator in enumerate(tee(iterable, n))  # magical 'enumerate' creates n a list of n deque copies
    ]
    return zip(*iterators)

"""
123456, 2
[deque(123456), dequeu(123456)]
123456
23456
12, 23, 34, 45, 56
"""