from textwrap import dedent
import unittest

from format_fixed_width import format_fixed_width


class FormatFixedWidthTests(unittest.TestCase):

    """Tests for format_fixed_width."""

    def test_single_list_with_single_element(self):
        self.assertEqual(format_fixed_width([["hello"]]), "hello")

    def test_single_list_with_two_elements(self):
        self.assertEqual(format_fixed_width([["hi", "there"]]), "hi  there")

    def test_two_lists_with_one_element_each(self):
        self.assertEqual(
            format_fixed_width([["Jane"], ["Mark"]]),
            "Jane\nMark"
        )

    def test_two_lists_with_two_elements_each(self):
        self.assertEqual(
            format_fixed_width([["Jane", "Austen"], ["Mark", "Twain"]]),
            dedent("""
                Jane  Austen
                Mark  Twain
            """).strip("\n")
        )

    def test_no_rows(self):
        self.assertEqual(format_fixed_width([]), "")

    def test_different_length_first_column(self):
        self.assertEqual(
            format_fixed_width([
                ["Jane", "Austen"],
                ["Mark", "Twain"],
                ["Charlotte", "Brontë"]
            ]),
            dedent("""
                Jane       Austen
                Mark       Twain
                Charlotte  Brontë
            """).strip("\n")
        )

    def test_missing_column_data(self):
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ]),
            dedent("""
                Jane               Austen
                Samuel  Langhorne  Clemens
                        Charlotte  Brontë
            """).strip("\n")
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_different_padding(self):
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], padding=1),
            dedent("""
                Jane             Austen
                Samuel Langhorne Clemens
                       Charlotte Brontë
            """).strip("\n")
        )
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], padding=3),
            dedent("""
                Jane                 Austen
                Samuel   Langhorne   Clemens
                         Charlotte   Brontë
            """).strip("\n")
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_column_widths_specified(self):
        self.assertEqual(
            format_fixed_width([
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], widths=[10, 10, 10]),
            dedent("""
                Samuel      Langhorne   Clemens
                            Charlotte   Brontë
            """).strip("\n")
        )
        self.assertEqual(
            format_fixed_width([
                ["Jane", "", "Austen"],
                ["Samuel", "Langhorne", "Clemens"],
                ["", "Charlotte", "Brontë"]
            ], widths=[8, 10, 10], padding=1),
            dedent("""
                Jane                Austen
                Samuel   Langhorne  Clemens
                         Charlotte  Brontë
            """).strip("\n")
        )

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_column_alignments(self):
        self.assertEqual(
            format_fixed_width([
                ['NN', 'Artist', 'Title', 'Time'],
                ['03', 'Paul Simon', 'Peace Like a River', '3:23'],
                ['16', 'Johnny Cash', 'Personal Jesus', '3:20'],
                ['', '', '', '1:09:32']
            ], alignments=['L', 'L', 'L', 'R']),
            dedent("""
                NN  Artist       Title                  Time
                03  Paul Simon   Peace Like a River     3:23
                16  Johnny Cash  Personal Jesus         3:20
                                                     1:09:32
            """).strip("\n")
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)