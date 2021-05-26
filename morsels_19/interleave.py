from itertools import chain


def interleave_0(a, b):
    """ Simple version """
    result = []
    for i, j in zip(a, b):
        result.append(i)
        result.append(j)
    return result


def interleave(a, b):
    """ Simple version ... I like this best because it is simple and clear"""
    for i, j in zip(a, b):
        yield i
        yield j


def interleave_generator_expression(iterable1, iterable2):
    """ I quite like this because it manages to use the zip and then turn that iterable of pairs into a new iterable"""
    return chain.from_iterable(zip(iterable1, iterable2))


def interleave_generator_expression2(iterable1, iterable2):
    """ I quite like this because it uses basic for loop unrolling to make a single comprehension"""
    return (
        item
        for pair in zip(iterable1, iterable2)
        for item in pair
    )
