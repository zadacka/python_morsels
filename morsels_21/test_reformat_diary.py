from contextlib import contextmanager
from io import StringIO
import os
from os.path import join
from glob import glob
from textwrap import dedent
from tempfile import TemporaryDirectory
import unittest

from morsels_21.reformat_diary import entries_by_date


class EntriesByDateTests(unittest.TestCase):

    """Tests for entries_by_date"""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_single_entry(self):
        diary = StringIO("2018-01-01\n\nI created a Python exercise today.")
        entries = entries_by_date(diary)
        self.assertIterableEqual(entries, [
            ("2018-01-01", "I created a Python exercise today."),
        ])

    def test_two_entries(self):
        diary = StringIO(dedent("""
            2018-01-01

            I created a Python exercise today.

            2018-01-02

            I slept all day
        """).lstrip())
        entries = entries_by_date(diary)
        self.assertIterableEqual(entries, [
            ("2018-01-01", "I created a Python exercise today."),
            ("2018-01-02", "I slept all day"),
        ])

    def test_multiline_entries(self):
        diary = StringIO(dedent("""
            2018-01-01

            I created a Python exercise today.  I also did laundry.

            I ate ice cream for dinner.  That wasn't a good idea.

            2018-01-02

            I slept all day today

            2018-01-04

            I forgot to journal on 2018-01-03.  Oh well.
        """).lstrip())
        entries = entries_by_date(diary)
        self.assertIterableEqual(entries, [
            ("2018-01-01",
             "I created a Python exercise today.  "
             "I also did laundry.\n\n"
             "I ate ice cream for dinner.  That wasn't a good idea."),
            ("2018-01-02", "I slept all day today"),
            ("2018-01-04", "I forgot to journal on 2018-01-03.  Oh well."),
        ])

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_clean_HTML_from_entries(self):
        diary = StringIO(dedent("""
            2018-01-01

            I said &quot;rabbit, rabbit&quot; today.

            2018-01-02

            I slept all day. &nbsp;I ate fish &amp; chips.
        """).lstrip())
        entries = entries_by_date(diary)
        self.assertIterableEqual(entries, [
            ("2018-01-01", 'I said "rabbit, rabbit" today.'),
            ("2018-01-02", "I slept all day.  I ate fish & chips."),
        ])


# To test the Bonus part of this exercise, comment out the following line
# @unittest.expectedFailure
class MainFunctionTests(unittest.TestCase):

    """Tests for main function"""

    def assertFileEquals(self, filename, contents):
        with open(filename) as text_file:
            self.assertEqual(text_file.read(), contents)

    def assertFilesAre(self, files):
        self.assertEqual(sorted(glob('*-*-*.txt')), files)

    def test_single_row(self):
        from reformat_diary import main
        contents = dedent("""
            2018-01-01

            I created a Python exercise today.

            2018-01-02

            I slept all day
        """).lstrip()
        with create_diary_files(contents) as (original, dirname):
            main(original)
            self.assertFilesAre([
                '2018-01-01.txt',
                '2018-01-02.txt',
            ])
            self.assertFileEquals(
                '2018-01-01.txt',
                "I created a Python exercise today.",
            )
            self.assertFileEquals(
                '2018-01-02.txt',
                "I slept all day",
            )

    def test_many_files(self):
        from reformat_diary import main
        contents = dedent("""
            2018-01-01

            Entry 1

            2018-01-02

            Entry 2

            2018-01-03

            Entry 3

            2018-01-04

            Entry 4

            2018-01-05

            Entry 5
        """).lstrip()
        with create_diary_files(contents) as (original, dirname):
            main(original)
            self.assertFilesAre([
                '2018-01-01.txt',
                '2018-01-02.txt',
                '2018-01-03.txt',
                '2018-01-04.txt',
                '2018-01-05.txt',
            ])
            self.assertFileEquals('2018-01-01.txt', "Entry 1")
            self.assertFileEquals('2018-01-02.txt', "Entry 2")
            self.assertFileEquals('2018-01-03.txt', "Entry 3")
            self.assertFileEquals('2018-01-04.txt', "Entry 4")
            self.assertFileEquals('2018-01-05.txt', "Entry 5")


@contextmanager
def chdir(directory):
    cwd = os.getcwd()
    os.chdir(directory)
    try:
        yield
    finally:
        os.chdir(cwd)


@contextmanager
def create_diary_files(contents):
    with TemporaryDirectory() as tmp_dirname:
        filename = join(tmp_dirname, "diary.txt")
        with open(filename, mode='wt') as diary:
            diary.write(contents)
        with chdir(tmp_dirname):
            yield filename, tmp_dirname


if __name__ == "__main__":
    unittest.main(verbosity=2)