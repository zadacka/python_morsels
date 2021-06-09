from contextlib import contextmanager, redirect_stdout
from io import StringIO
import imp
import os
import sys
from textwrap import dedent
from tempfile import NamedTemporaryFile
import unittest


class UnicodeEscapeTests(unittest.TestCase):

    """Tests for unicode_esacpe.py"""

    def test_no_escaping_needed(self):
        with make_file("print('hello world')") as filename:
            output = run_program('unicode_escape.py', args=[filename])
        self.assertEqual("print('hello world')", output)

    def test_one_escaped_character(self):
        with make_file("print('\U0001f31f')") as filename:
            output = run_program('unicode_escape.py', args=[filename])
        self.assertEqual(r"print('\U0001f31f')", output)

    def test_already_escaped_characters(self):
        contents = r"print('\U0001f31f!')"
        with make_file(contents) as filename:
            output = run_program('unicode_escape.py', args=[filename])
        self.assertEqual(contents, output)

    def test_multiple_lines_and_multiple_characters(self):
        contents = dedent("""
            Heartbeat \U0001f493,
            Sparkle heart \U0001f496.
            Watermelon \U0001f349,
            Penguin \U0001f427!
        """).lstrip()
        expected = dedent(r"""
            Heartbeat \U0001f493,
            Sparkle heart \U0001f496.
            Watermelon \U0001f349,
            Penguin \U0001f427!
        """).lstrip()
        with make_file(contents) as filename:
            output = run_program('unicode_escape.py', args=[filename])
        self.assertEqual(expected, output)

    def test_original_file_is_unchanged(self):
        contents = r"print('hello world!')"
        with make_file(contents) as filename:
            output = run_program('unicode_escape.py', args=[filename])
            with open(filename, mode='rt') as temp_file:
                assert temp_file.read() == contents
        self.assertEqual(contents, output)

    # @unittest.expectedFailure
    def test_small_hex_values(self):
        with make_file("print('\xa0\u263a\U0000263a')") as filename:
            output = run_program('unicode_escape.py', args=[filename])
        self.assertEqual(r"print('\u00a0\u263a\u263a')", output)

    # @unittest.expectedFailure
    def test_standard_input(self):
        with patch_stdin("print('\u263a\U0000263a')"):
            output = run_program('unicode_escape.py', args=['-'])
        self.assertEqual(r"print('\u263a\u263a')", output)

    # @unittest.expectedFailure
    def test_different_styles(self):
        with make_file("print('\u00a9\u263a\U0001f31f')") as filename:
            output = run_program('unicode_escape.py',
                                 args=[filename, '--style=html'])
        self.assertEqual(r"print('&#xa9;&#x263a;&#x1f31f;')", output)


class DummyException(Exception):
    """Nothing should ever raise this."""


def run_program(path, args=[], raises=DummyException):
    old_args = sys.argv
    assert all(isinstance(a, str) for a in args)
    try:
        sys.argv = [path] + args
        with redirect_stdout(StringIO()) as output:
            try:
                if '__main__' in sys.modules:
                    del sys.modules['__main__']
                imp.load_source('__main__', path)
            except raises:
                return output.getvalue()
            except SystemExit as e:
                if e.args != (0,):
                    raise
            if raises is not DummyException:
                raise AssertionError("{} not raised".format(raises))
            return output.getvalue()
    finally:
        sys.argv = old_args


@contextmanager
def patch_stdin(contents):
    old_stdin = sys.stdin
    sys.stdin = StringIO(contents)
    try:
        yield
    finally:
        sys.stdin = old_stdin


@contextmanager
def make_file(contents=None):
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)