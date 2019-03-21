from calendar import monthrange
from datetime import date
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    _, last_day = monthrange(year, month)
    days_in_month = [date(year, month, day) for day in range(1, last_day + 1)]
    weekdays_of_interest = [d for d in days_in_month if d.weekday() == weekday]

    zero_based_index = nth if nth < 0 else nth - 1
    return weekdays_of_interest[zero_based_index]


def weekdays_in_month(year, month, weekday):
    """
    Return list of all 4/5 dates with given weekday and year/month.
    from_morsels_solution - I like the way that this uses Calendar
    ... although without having seen that library before, my approach (above)
    feels more immediately readable (though probably less efficient)!
    """
    from calendar import Calendar
    return [
        dates[0]
        for dates in Calendar(weekday).monthdatescalendar(year, month)
        if dates[0].month == month
    ]