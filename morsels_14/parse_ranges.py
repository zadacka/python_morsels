def parse_ranges_my_solution(ranges):
    """
    Output strings of ranges like so:
     >> parse_ranges('1, 2-7, 8-8, 9->end':
     1, 2, 3, 4, 5, 6, 7, 8, 9

    """
    for range_part in ranges.split(','):
        if '->' in range_part:
            number, _ = range_part.split('->')
            yield int(number)
        elif '-' in range_part:
            start, end = range_part.split('-')
            yield from range(int(start), int(end) + 1)
        else:
            yield int(range_part)


def parse_ranges(ranges):
    def partition(sep, group):
        import re
        group = re.sub(r'->.*', r'', group)
        a, _, b = group.partition(sep)
        return (a, b) if b else (a, a)

    pairs = (
        partition('-', group)
        for group in ranges.split(',')
    )

    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop) + 1)
    )
