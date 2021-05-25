import _csv
import csv
from collections import defaultdict
from itertools import zip_longest


def csv_columns(csvfile, *, headers=None, missing=None):
    """ Trey approved """
    columns = defaultdict(list)
    reader = csv.DictReader(csvfile, fieldnames=headers, restval=missing)
    for row in reader:
        for name, value in row.items():
            columns[name].append(value)
    return columns


def csv_columns_runner_up(csvfile, *, headers=None, missing=None):
    """ Another of Trey's - I like this one because of the neat unpacking and use of zip_longest"""
    columns = defaultdict(list)
    reader = csv.reader(csvfile)
    if headers is None:
        headers = next(reader)
    columns = zip_longest(*reader, fillvalue=missing)
    return {
        header: list(column)
        for header, column in zip(headers, columns)
    }


def csv_columns_alex(csvfile, headers=None, missing=None):
    """ Alex's attempt """
    try:
        dialect = csv.Sniffer().sniff(csvfile.readline(), delimiters=",")
    except _csv.Error:
        dialect = 'excel'

    headers = headers if headers else []
    result = {h: [] for h in headers}

    csvfile.seek(0)
    for f in csv.reader(csvfile, dialect):
        if result:
            for key, value in zip_longest(result.keys(), f, fillvalue=missing):
                result[key].append(value)
        else:
            result = {header: [] for header in f}
    return result


def csv_columns_nice_tuple_unpacking(csv_file):
    """Neat Trey trick of splatting the reader columns, then zipping through the rows."""
    reader = csv.reader(csv_file)
    headers = next(reader)
    return {
        header: column
        for header, *column in zip(headers, *reader)
    }
