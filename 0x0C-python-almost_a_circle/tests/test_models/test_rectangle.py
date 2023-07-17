#!/usr/bin/python3
"""Unittests for rectangle.py.

Unittests classes:
    TestRectangle_init - line 21
    TestRectangle_validation - line 103
    TestRectangle_area - line 239
    TestRectangle_display - line 271
    TestRectangle_update - line 329
    TestRectangle_to_dictionary - line 455
"""
import os
import json
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):
    """Tests the instantiation of the Rectangle class."""

    def test_rectange_is_base(self):
        """Assert that a rectangle is an instance of the Base class."""
        self.assertIsInstance(Rectangle(10, 10), Base)

    def test_rectangle_init(self):
        """Tests instantiation of a rectangle."""

        r1 = Rectangle(10, 2)

        r2 = Rectangle(2, 5, 1)
        self.assertEqual(r2.id, r1.id + 1)

        r3 = Rectangle(7, 3, 0, 1)
        self.assertEqual(r3.id, r1.id + 2)

        r4 = Rectangle(12, 9, 4, 0, 15)
        self.assertEqual(r4.id, 15)

    def test_rectangle_private(self):
        """Asserts that a rectangle's attributes are private."""

        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__width_)

        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__height)

        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__x)

        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__y)

    def test_rectangle_getters(self):
        """Tests the rectangle's getters."""

        r1 = Rectangle(7, 3, 5, 1)

        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 1)

        r2 = Rectangle(10, 10)

        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_rectangle_setters(self):
        """Test the rectangle's setters."""

        r = Rectangle(12, 9, 4, 0, 15)
        self.assertEqual(str(r), "[Rectangle] (15) 4/0 - 12/9")

        r.width = 20
        self.assertEqual(str(r), "[Rectangle] (15) 4/0 - 20/9")

        r.height = 8
        self.assertEqual(str(r), "[Rectangle] (15) 4/0 - 20/8")

        r.x = 7
        self.assertEqual(str(r), "[Rectangle] (15) 7/0 - 20/8")

        r.y = 8
        self.assertEqual(str(r), "[Rectangle] (15) 7/8 - 20/8")

    def test_rectangle_init_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            A rectangle is instantiated with at least two and at most five
            arguments.
        """
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)


class TestRectangle_validation(unittest.TestCase):
    """Tests the validation of attributes of a Rectangle instance."""

    def test_validation_width(self):
        """Tests width validation."""

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, "10", 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, None, 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, "12.5", 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, (1, 2), 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, {1, 2}, 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, True, 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, [1, 2, 3], 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, float('inf'), 2)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, float('nan'), 2)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Rectangle, 0, 2)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Rectangle, -3, 2)

    def test_validation_height(self):
        """Tests height validation."""

        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, "10")
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, None)
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, "12.5")
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, (1, 2))
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, {1, 2})
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, True)
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, [1, 2, 3])
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, float('inf'))
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 3, float('nan'))
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               Rectangle, 3, 0)
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               Rectangle, 3, -3)

    def test_validation_x(self):
        """Tests x validation."""

        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, "10")
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, None)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, "12.5")
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, (1, 2))
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, {1, 2})
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, True)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, [1, 2, 3])
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, float('inf'))
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 3, 5, float('nan'))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               Rectangle, 3, 5, -3)

    def test_validation_y(self):
        """Tests y validation."""

        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, "10")
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, None)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, "12.5")
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, (1, 2))
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, {1, 2})
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, True)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, [1, 2, 3])
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, float('inf'))
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 3, 5, 0, float('nan'))
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               Rectangle, 3, 5, 0, -3)

    def test_validation_order(self):
        """Tests the validation order.

            Attributes are validated in this order: width, height, x, y.
        """
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, "invalid width", "invalid height",
                               "invalid x", "invalid y")

        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Rectangle, 0, "invalid height",
                               "invalid x", "invalid y")

        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 2, "invalid height",
                               "invalid x", "invalid y")

        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               Rectangle, 2, -3, "invalid x", "invalid height")

        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 2, 4, "invalid x", "invalid y")

        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               Rectangle, 2, 4, -3, "invalid y")

        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 2, 4, 0, "invalid y")

        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               Rectangle, 2, 4, 0, -6)


class TestRectangle_area(unittest.TestCase):
    """Tests the area method."""

    def test_area_small(self):
        """Tests the area method with small numbers."""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area_large(self):
        """Tests the area method with large numbers."""

        r2 = Rectangle(999999999999999999999999999999,
                       99999999999999999999999999999999)
        self.assertEqual(r2.area(), int('9999999999999999999999999999'
                         '9899000000000000000000000000000001'))

    def test_area_update(self):
        """Tests the area method after an attribute change."""
        r1 = Rectangle(10, 10)
        r1.width = 100
        self.assertEqual(r1.area(), 1000)

    def test_area_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            area takes no arguments.
        """
        r = Rectangle(3, 4)
        self.assertRaises(TypeError, r.area, 1)


class TestRectangle_display(unittest.TestCase):
    """Tests the display method."""

    def assert_output(self, rect, expected):
        """Checks for expected output on stdout for the display method.

            Args:
                rect (Rectangle): the rectangle to display.
                expected (str): the expected output.
        """

        with patch('sys.stdout', new=StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display(self):
        """Tests the display method."""

        r1 = Rectangle(4, 6)
        expected = "####\n####\n####\n####\n####\n####\n"
        self.assert_output(r1, expected)

        r2 = Rectangle(1, 1)
        expected = "#\n"
        self.assert_output(r2, expected)

        r3 = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assert_output(r3, expected)

        r4 = Rectangle(1, 1, 1, 1)
        expected = "\n #\n"
        self.assert_output(r4, expected)

    def test_display_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            display takes no arguments.
        """
        r = Rectangle(3, 4)
        self.assertRaises(TypeError, r.display, 1)

    def test_string_repr(self):
        """Tests the string representation of a rectangle."""
        r1 = Rectangle(3, 4, 5, 6, 7)
        expected = "[Rectangle] (7) 5/6 - 3/4"
        self.assertEqual(str(r1), expected)

        r1.width = 100
        r1.height = 20
        r1.x = 15
        r1.y = 8
        expected = "[Rectangle] (7) 15/8 - 100/20"
        self.assertEqual(str(r1), expected)

        self.assertRaises(TypeError, r1.__str__, 1)


class TestRectangle_update(unittest.TestCase):
    """Tests the update method."""

    def test_update_args(self):
        """Tests the update method with *args only."""

        r1 = Rectangle(10, 10, 10, 10, 1)

        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(None)
        self.assertEqual(str(r1),
                         "[Rectangle] ({}) 10/10 - 10/10".format(r1.id))

        r1.update(1, 2)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 2/10")

        r1.update(3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (3) 10/10 - 4/5")

        r1.update(6, 7, 8, 9)
        self.assertEqual(str(r1), "[Rectangle] (6) 9/10 - 7/8")

        r1.update(99, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (99) 4/5 - 2/3")

        r1.update(10, 20, 30, 40, 50, 60)
        self.assertEqual(str(r1), "[Rectangle] (10) 40/50 - 20/30")

    def test_update_validation_args(self):
        """Tests update *args validation.

            Validation is performed for all updated attributes except id.
        """

        r1 = Rectangle(1, 2, 3, 4, 5)

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               r1.update, None, None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               r1.update, 15, 0)
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               r1.update, 15, 3, "hello")
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               r1.update, 15, 3, -5)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               r1.update, 15, 3, 5, (1, 2))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               r1.update, 15, 3, 8, -2)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               r1.update, 15, 3, 8, 0, {"set", "set2"})
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               r1.update, 15, 3, 8, 0, -4)

    def test_update_kwargs(self):
        """Tests the update method with **kwargs."""

        r1 = Rectangle(10, 20, 30, 40, 50)

        r1.update(id=None)
        expected = "[Rectangle] ({}) 30/40 - 10/20".format(r1.id)
        self.assertEqual(str(r1), expected)

        r1.update(id=89, height=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 30/40 - 10/1")

        r1.update(id=90, height=10, x=5)
        self.assertEqual(str(r1), "[Rectangle] (90) 5/40 - 10/10")

        r1.update(id=2, height=11, x=8, width=7)
        self.assertEqual(str(r1), "[Rectangle] (2) 8/40 - 7/11")

        r1.update(x=1, y=19, height=2, width=4, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/19 - 4/2")

    def test_update_validation_kwargs(self):
        """Tests update **kwargs validation.

            Validation is performed for all updated attributes except id.
        """

        r1 = Rectangle(1, 2, 3, 4, 5)

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               r1.update, width=None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               r1.update, id=90, width=0)
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               r1.update, id=89, width=5, height="hello")
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               r1.update, height=-3)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               r1.update, height=8, x=(1, 2))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               r1.update, x=-2)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               r1.update, y={"set", "set2"}, width=20)
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               r1.update, id=15, height=2, y=-3)

    def test_update_args_kwargs(self):
        """Tests the update method with *args and **kwargs.

            **kwargs is ignored if *args is provided.
        """
        r = Rectangle(1, 2, 3, 4, 5)

        r.update(10, 20, 30, id=90, width=40)
        self.assertEqual(str(r), "[Rectangle] (10) 3/4 - 20/30")

    def test_update_kwargs_wrong_keys(self):
        """Tests the update method with the wrong keys for **kwargs."""

        r = Rectangle(1, 2, 3, 4, 5)

        r.update(h=1, w=2)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

        r.update(id=90, height=30, a=3, b=4)
        self.assertEqual(str(r), "[Rectangle] (90) 3/4 - 1/30")


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests the to dictionary method."""

    def test_to_dictionary(self):
        """Test the to_dictionary method."""

        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertDictEqual(r1_dict, expected)

        r1.update(10, 20, 30, 40)
        r1_dict = r1.to_dictionary()
        expected = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 9}
        self.assertDictEqual(r1_dict, expected)

        r2 = Rectangle(1, 1, 0, 0, 2)
        r2_dict = r2.to_dictionary()
        expected = {"id": 2, "width": 1, "height": 1, "x": 0, "y": 0}
        self.assertDictEqual(r2_dict, expected)

    def test_to_dictionary_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            to_dictionary takes no arguments.
        """
        r = Rectangle(10, 10)
        self.assertRaises(TypeError, r.to_dictionary, 1)


if __name__ == "__main__":
    unittest.main()
