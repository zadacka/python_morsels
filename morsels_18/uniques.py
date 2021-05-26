def is_hashable(input):
    try:
        hash(input)
    except TypeError:
        return False
    return True


def uniques_only_1(input):
    """ Simple implementation"""
    seen = set()
    for i in input:
        if i not in seen:
            yield i
        seen.add(i)


def uniques_only(input):
    """ Cope with non-hashables"""
    seen = set()
    hashable = True
    for i in input:
        if not is_hashable(i):
            # one or more items is not hashable - switch to a list
            seen = list(seen)
            hashable = False
        if i in seen:
            continue

        yield i
        seen.add(i) if hashable else seen.append(i)


def uniques_only_trey_oneline(iterable):
    """Return iterable in the same order but with duplicates removed.
        This works in Python 3.6+ since dictionaries are ordered
    """
    return dict.fromkeys(iterable).keys()


def uniques_only_trey_folution(iterable):
    """ I really like this for the following reasons:
        1) a nice, clear hashable check
        2) no 'magic' switching
        3) handles iterables of mixed hashable / un-hashable items with no performance penalty
    """
    seen_hashable = set()
    seen_unhashable = list()
    from collections.abc import Hashable
    for i in iterable:
        if isinstance(i, Hashable):
            if i not in seen_hashable:
                yield i
                seen_hashable.add(i)
        else:
            if i not in seen_unhashable:
                yield i
                seen_unhashable.append(i)
