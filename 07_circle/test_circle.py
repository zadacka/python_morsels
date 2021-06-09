import math
import unittest

from circle import Circle


class CircleTests(unittest.TestCase):

    """Tests for Circle."""

    def test_radius(self):
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)

    def test_default_radius(self):
        circle = Circle()
        self.assertEqual(circle.radius, 1)

    def test_diameter(self):
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)

    def test_area(self):
        circle = Circle(2)
        self.assertEqual(circle.area, math.pi * 4)
        circle = Circle(1)
        self.assertEqual(circle.area, math.pi)

    def test_string_representation(self):
        circle = Circle(2)
        self.assertEqual(str(circle), 'Circle(2)')
        self.assertEqual(repr(circle), 'Circle(2)')
        circle.radius = 1
        self.assertEqual(repr(circle), 'Circle(1)')

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_diameter_and_area_change_based_on_radius(self):
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)
        circle.radius = 3
        self.assertEqual(circle.diameter, 6)
        self.assertEqual(circle.area, math.pi * 9)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_diameter_changeable_but_area_not(self):
        circle = Circle(2)
        self.assertEqual(circle.diameter, 4)
        self.assertEqual(circle.area, math.pi * 4)
        circle.diameter = 3
        self.assertEqual(circle.radius, 1.5)
        with self.assertRaises(AttributeError):
            circle.area = 3

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_no_negative_radius(self):
        circle = Circle(2)
        with self.assertRaises(ValueError) as context:
            circle.radius = -10
        self.assertEqual(str(context.exception), "Radius cannot be negative")


if __name__ == "__main__":
    unittest.main()