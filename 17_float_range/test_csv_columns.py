from io import StringIO
from textwrap import dedent
import unittest

from morsels_17.csv_columns import csv_columns


unittest.util._MAX_LENGTH = 300


class CSVColumnsTests(unittest.TestCase):

    """Tests for csv_columns."""

    maxDiff = None

    def test_single_column(self):
        result = {'h1': ['1', '2']}
        self.assertEqual(
            csv_columns(StringIO('h1\r\n1\r\n2\r\n')),
            result
        )

    def test_two_columns(self):
        result = {'h1': ['1', '3'], 'h2': ['2', '4']}
        self.assertEqual(
            csv_columns(StringIO('h1,h2\r\n1,2\r\n3,4\r\n')),
            result
        )

    def test_three_columns(self):
        csv_data = dedent("""
            Year,Make,Model
            2012,Lexus,LFA
            2009,GMC,Yukon XL 1500
            1965,Ford,Mustang
            2005,Hyundai,Sonata
            1995,Mercedes-Benz,C-Class
        """).lstrip()
        result = {
            'Year': ['2012', '2009', '1965', '2005', '1995'],
            'Make': ['Lexus', 'GMC', 'Ford', 'Hyundai', 'Mercedes-Benz'],
            'Model': ['LFA', 'Yukon XL 1500', 'Mustang', 'Sonata', 'C-Class'],
        }
        self.assertEqual(csv_columns(StringIO(csv_data)), result)

    def test_commas_in_data(self):
        result = {'header, 1': ['1', '3,4'], 'h2': ['2', '4']}
        self.assertEqual(
            csv_columns(StringIO('"header, 1",h2\r\n1,2\r\n"3,4",4\r\n')),
            result
        )

    def test_file_is_left_open(self):
        """Make sure csv_columns doesn't close the file given to it."""
        csv_file = StringIO('h1\r\n1\r\n2\r\n')
        csv_columns(csv_file)  # Read it once
        csv_file.seek(0)  # Seek to the beginning of the still-open file
        self.assertEqual(csv_columns(csv_file), {'h1': ['1', '2']})

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_ordered_dictionary(self):
        csv_data = dedent("""
            Car 1,Car 2,Car 3,Car 4,Car 5
            2012,2009,1965,2005,1995
            Lexus,GMC,Ford,Hyundai,Mercedes-Benz
            LFA,Yukon XL 1500,Mustang,Sonata,C-Class
        """).lstrip()
        result = [
            ('Car 1', ['2012', 'Lexus', 'LFA']),
            ('Car 2', ['2009', 'GMC', 'Yukon XL 1500']),
            ('Car 3', ['1965', 'Ford', 'Mustang']),
            ('Car 4', ['2005', 'Hyundai', 'Sonata']),
            ('Car 5', ['1995', 'Mercedes-Benz', 'C-Class']),
        ]
        self.assertEqual(list(csv_columns(StringIO(csv_data)).items()), result)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_key_word_headers(self):
        result_with_given_headers = {
            'header1': ['1', '3'],
            'header2': ['2', '4'],
        }
        result_with_default = {'1': ['3'], '2': ['4']}
        csv_file = StringIO('1,2\r\n3,4\r\n')
        self.assertEqual(
            csv_columns(csv_file, headers=['header1', 'header2']),
            result_with_given_headers
        )
        csv_file.seek(0)
        self.assertEqual(csv_columns(csv_file), result_with_default)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_allow_missing_items(self):
        result_zero_given = {'h1': ['1', '3', '5'], 'h2': ['2', '4', '0']}
        result_nothing_given = {'h1': ['1', '3', '5'], 'h2': ['2', '4', None]}
        self.assertEqual(
            csv_columns(StringIO('h1,h2\r\n1,2\r\n3,4\r\n5\r\n'), missing='0'),
            result_zero_given
        )
        self.assertEqual(
            csv_columns(StringIO('h1,h2\r\n1,2\r\n3,4\r\n5\r\n')),
            result_nothing_given
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)