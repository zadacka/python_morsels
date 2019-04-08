from collections import Iterable


def deep_add_my_version(input_structure, start=None):
    """
    Yuk yuk yuk!! I puzzled through to get 'something that works', and then
    read through Trey's solution to see how it could be done better

    Key learning points:
    1. Once again, using sum() to avoid the bother of having a 'total' variable is
       awesome, especially as it completely side-steps the problem of what type the
       variable should be in order to get addition to work correctly!!
    2. isinstance(<thing to check>, collections.Iterable) is awesome, especially given
       the magical behaviour of the Iterable class (which uses __subclasscheck__ to know
       what is an iterable and what is not - so even works for user defined classes)
    3. Python Morsels are flipping awesome. The 'good' way to do this is so much better
       than my initial stab, and the step-by-step instructions really help explain the
       differences...
    """
    result = start or None

    if isinstance(input_structure, list) and len(input_structure) == 0:
        return 0

    for element in input_structure:
        if isinstance(element, Iterable):
            if result is None:
                result = deep_add(element)
            else:
                result += deep_add(element)
        else:
            if result is None:
                result = element
            else:
                result += element
    return result


def deep_add(list_or_number, start=0):
    if isinstance(list_or_number, Iterable):
        return sum((deep_add(x) for x in list_or_number), start)
    else:
        return list_or_number
