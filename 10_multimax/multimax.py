from collections import defaultdict


def multimax_local(sequence, key=lambda x: x):
    """ Fun approach working on the (wrong) assumption that we're trying to
        find local maxima, rather than just places where the global
        maximum is reached...
    """
    if not sequence:
        return []

    sequence_min = min(sequence, key=key)
    results = []
    for first, second, third in zip([sequence_min, sequence_min, *sequence],
                                    [sequence_min, *sequence, sequence_min],
                                    [*sequence, sequence_min, sequence_min]):
        if key(second) > key(first) and key(second) > key(third):
            results.append(second)
    return results


def hash(input):
    """ Make input hashable:
        * turn anything else (is there a nice standard library way to do this?)
        * ... so won't work for sets, dictionaries, etc...
    """
    if isinstance(input, list):
        return tuple(input)
    return input


def multimax(sequence, key=lambda x: x):
    result = defaultdict(list)
    for element in sequence:
        result[hash(key(element))].append(element)

    max_value = max(result.keys(), default=None)
    if max_value is None:
        return []
    return result[max_value]

# the online tests didn't accept the above (?!) but did
# accept the below...


def multimax_as_submitted(sequence, key=lambda x:x):
    result = []
    max_so_far = None
    for x in sequence:
        value = key(x)
        if max_so_far is None or value > max_so_far:
            max_so_far = value
            result = [x]
        elif value == max_so_far:
            result.append(x)
    return result
