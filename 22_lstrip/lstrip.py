# I want you to write a function that accepts an iterable and an object and returns a new iterable with all items
# from the original iterable except any item at the beginning of the iterable which is equal to the object should
# be skipped.

def is_equal(value, comparator):
    """ Test equality of callable on value OR equality of value object to comparator"""
    return comparator(value) if callable(comparator) else value == comparator


def lstrip_simple_but_incomplete(iterable, strip_value):
    return (i for i in iterable if not is_equal(i, strip_value))


def lstrip_alex(iterable, strip_value):
    do_strip = True
    for i in iterable:
        if do_strip and is_equal(i, strip_value):
            continue
        do_strip = False
        yield i


def lstrip(iterable, strip_value):
    iterator = iter(iterable)  # need to do this so we can 'next' or 'yield from' the input
    for i in iterator:
        # fast forward through things until we hit something different from the strip value, then yield and break
        if not is_equal(i, strip_value):
            yield i
            break
    # neat Py3 syntax instead of "for i in iterator: yield i"
    yield from iterator


def lstrip_trey1(iterable, strip_value):
    from itertools import dropwhile
    # of course, itertools has something that does what we want: "dropwhile" which works on iterables
    def is_strip_value(v): return strip_value(v) if callable(strip_value) else v is strip_value

    return dropwhile(is_strip_value, iterable)
