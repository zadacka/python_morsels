def format_fixed_width_alex(rows, padding=2, widths=None, alignments=None):
    result = ""

    if widths is None:
        widths = [max(len(item) for item in column) for column in zip(*rows)]

    if alignments is None:
        alignments = ['L'] * len(widths)

    first = True
    for row in rows:
        if first:
            first = False
        else:
            result += '\n'

        for item, longest_word, alignment in zip(row, widths, alignments):
            align = '<' if alignment == 'L' else '>'
            width = longest_word + padding if alignment == 'L' else longest_word
            result += "{0:{fill}{align}{width}}".format(item, fill=' ', align=align, width=width)
        result = result.rstrip()
    return result


def format_fixed_width(rows, padding=2, widths=None, alignments=None):

    def justify_columns(row, column_widths, alignments):
        """ split out alignment logic - nice, makes use within a comprehension cleaner """
        return [
            cell.ljust(column_width) if alignment == 'L' else cell.rjust(column_width)  # neat use of ljust() or rjust()
            for cell, column_width, alignment in zip(row, column_widths, alignments)
        ]

    if widths is None:
        # I'm proud that I'd worked out how to do this too...
        widths = [
            max(len(cell) for cell in column)
            for column in zip(*rows)
        ]

    if alignments is None:
        # and this!
        alignments = ['L'] * len(widths)

    joiner = " " * padding

    return "\n".join(
        # use of a 'joiner' and doing a cell join solves some of the problems I'd had: how to OMIT the terminal \n
        # and how to handle the alignment issue of a rjust col following an ljust col - in which case string padding
        # doesn't work quite right
        joiner.join(justify_columns(row, widths, alignments)).rstrip()
        for row in rows
    )
