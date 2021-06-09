from itertools import zip_longest


def add_with_try_catch(*args):
    result = []
    try:
        for lists in zip_longest(*args):
            result_list = []
            for elements in zip_longest(*lists):
                result_list.append(sum(elements))
            result.append(result_list)
    except TypeError as ex:
        raise ValueError from ex

    return result


def add_with_two_lengths_checks(*args):

    def raise_if_lengths_differ(lists):
        if any(len(args[0]) != len(l) for l in lists):
            raise ValueError("Length of elements do not match.")

    raise_if_lengths_differ(args)
    result = []
    for lists in zip(*args):
        raise_if_lengths_differ(lists)
        result_list = []
        for elements in zip(*lists):
            result_list.append(sum(elements))
        result.append(result_list)

    return result


def add(*args):
    """
    My favourite answer, based in part on the solutions:
    * uses a nested list comprehension in order to build the combined result
    * uses 'matrix shape' local method to clearly get matrix shapes
    * uses set of matrix shapes to determine whether to raise a ValueError or not
    """
    def matrix_shape(matrix):
        return tuple(len(row) for row in matrix)

    if len(set(matrix_shape(m) for m in args)) > 1:
        raise ValueError("Cannot add matrices of different sizes")

    combined = [
        [sum(elements) for elements in zip(*rows)]
        for rows in zip(*args)
    ]
    return combined
