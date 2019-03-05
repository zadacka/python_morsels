def get_earliest_attempt(*dates):
    """ issues:
    * adheres to nonsense spec (cope with invalid dates)
    * returns nonsense if there are no dates
    * does no validation
    """
    earliest_date = ('9999', '99', '99')

    for date in dates:
        month, day, year = date.split('/')
        if (year, month, day) < earliest_date:
            earliest_date = (year, month, day)

    return '{1}/{2}/{0}'.format(*earliest_date)


def get_earliest(*dates):
    """best solution """

    def date_key(date):
        (m, d, y) = date.split('/')
        return y, m, d

    return min(dates, key=date_key)


# Thoughts:
# * tuple unpacking is really nice
# * if you want the min of an iterable, use the min builtin!
