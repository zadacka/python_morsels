from collections import defaultdict


def group_by(iterable, key_func=lambda x:x):
    result = defaultdict(list)
    for element in iterable:
        result[key_func(element)].append(element)
    return result
