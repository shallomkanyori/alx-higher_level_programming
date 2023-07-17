#!/usr/bin/python3
"""Unittests for square.py.

Unittests classes:
    TestSquare_init - line 21
    TestSquare_validation - line 103
    TestSquare_area - line 239
    TestSquare_display - line 271
    TestSquare_update - line 329
    TestSquare_to_dictionary - line 455
"""
import os
import json
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare_init(unittest.TestCase):
    """Tests the instantiation of the Square class."""

    def test_square_is_base(self):
        """Assert that a square is an instance of the Base class."""
        self.assertIsInstance(Square(10), Base)

    def test_square_is_base(self):
        """Assert that a square is an instance of the Rectangle class."""
        self.assertIsInstance(Square(10), Rectangle)

    def test_square_init(self):
        """Tests instantiation of a square."""

        s1 = Square(10)

        s2 = Square(2, 5)
        self.assertEqual(s2.id, s1.id + 1)

        s3 = Square(7, 3, 0)
        self.assertEqual(s3.id, s1.id + 2)

        s4 = Square(12, 9, 4, 0)
        self.assertEqual(s4.id, 0)

    def test_square_private(self):
        """Asserts that a square's attributes are private."""

        with self.assertRaises(AttributeError):
            print(Square(10).__width_)

        with self.assertRaises(AttributeError):
            print(Square(10).__height)

        with self.assertRaises(AttributeError):
            print(Square(10).__x)

        with self.assertRaises(AttributeError):
            print(Square(10).__y)

        with self.assertRaises(AttributeError):
            print(Square(10).__size)

    def test_square_getters(self):
        """Tests the square's getters."""

        s1 = Square(7, 3, 5)

        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 5)

        s2 = Square(10)

        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

    def test_square_setters(self):
        """Test the square's setters."""

        s = Square(12, 9, 4, 15)
        self.assertEqual(str(s), "[Square] (15) 9/4 - 12")

        s.width = 20
        self.assertEqual(str(s), "[Square] (15) 9/4 - 20")

        s.size = 100
        self.assertEqual(str(s), "[Square] (15) 9/4 - 100")

        s.x = 7
        self.assertEqual(str(s), "[Square] (15) 7/4 - 100")

        s.y = 2
        self.assertEqual(str(s), "[Square] (15) 7/2 - 100")

    def test_square_init_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            A square is instantiated with at least one and at most four
            arguments.
        """
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5)


class TestSquare_validation(unittest.TestCase):
    """Tests the validation of attributes of a Square instance."""

    def test_validation_size(self):
        """Tests size validation."""

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, "10")
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, None)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, "12.5")
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, (1, 2))
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, {1, 2})
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, True)
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, [1, 2, 3])
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, float('inf'))
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, float('nan'))
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Square, 0)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Square, -3)

    def test_validation_x(self):
        """Tests x validation."""

        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, "10")
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, None)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, "12.5")
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, (1, 2))
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, {1, 2})
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, True)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, [1, 2, 3])
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, float('inf'))
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 3, float('nan'))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               Square, 3, -3)

    def test_validation_y(self):
        """Tests y validation."""

        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, "10")
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, None)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, "12.5")
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, (1, 2))
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, {1, 2})
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, True)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, [1, 2, 3])
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, float('inf'))
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 3, 0, float('nan'))
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               Square, 3, 0, -3)

    def test_validation_order(self):
        """Tests the validation order.

            Attributes are validated in this order: width, height, x, y.
        """
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, "invalid size", "invalid x",
                               "invalid y")

        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Square, 0, "invalid x", "invalid y")

        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 2, "invalid x", "invalid y")

        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               Square, 2, -3, "invalid y")

        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 2, 0, "invalid y")

        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               Square, 2, 0, -6)


class TestSquare_area(unittest.TestCase):
    """Tests the area method."""

    def test_area_small(self):
        """Tests the area method with small numbers."""

        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_area_large(self):
        """Tests the area method with large numbers."""

        s2 = Square(99999999999999999999999999999999999999)
        self.assertEqual(s2.area(), int('9999999999999999999999999999999999'
                         '999800000000000000000000000000000000000001'))

    def test_area_update(self):
        """Tests the area method after an attribute change."""
        s1 = Square(10)
        s1.size = 100
        self.assertEqual(s1.area(), 10000)

    def test_area_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            area takes no arguments.
        """
        r = Square(3)
        self.assertRaises(TypeError, r.area, 1)


class TestSquare_display(unittest.TestCase):
    """Tests the display method."""

    def assert_output(self, sq, expected):
        """Checks for expected output on stdout for the display method.

            Args:
                sq (Square): the square to display.
                expected (str): the expected output.
        """

        with patch('sys.stdout', new=StringIO()) as fake_out:
            sq.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display(self):
        """Tests the display method."""

        s1 = Square(4)
        expected = "####\n####\n####\n####\n"
        self.assert_output(s1, expected)

        s2 = Square(1, 1)
        expected = " #\n"
        self.assert_output(s2, expected)

        s3 = Square(2, 3, 2)
        expected = "\n\n   ##\n   ##\n"
        self.assert_output(s3, expected)

        s4 = Square(1, 1, 1, 1)
        expected = "\n #\n"
        self.assert_output(s4, expected)

    def test_display_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            display takes no arguments.
        """
        s = Square(3)
        self.assertRaises(TypeError, s.display, 1)

    def test_string_repr(self):
        """Tests the string representation of a square."""
        s1 = Square(3, 4, 5, 6)
        expected = "[Square] (6) 4/5 - 3"
        self.assertEqual(str(s1), expected)

        s1.size = 20
        s1.x = 15
        s1.y = 8
        expected = "[Square] (6) 15/8 - 20"
        self.assertEqual(str(s1), expected)

        self.assertRaises(TypeError, s1.__str__, 1)


class TestSquare_update(unittest.TestCase):
    """Tests the update method."""

    def test_update_args(self):
        """Tests the update method with *args only."""

        s1 = Square(10, 10, 10, 10)

        s1.update()
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")

        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")

        s1.update(None)
        expected = "[Square] ({}) 10/10 - 10".format(s1.id)
        self.assertEqual(str(s1), expected)

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 10/10 - 2")

        s1.update(3, 4, 5)
        self.assertEqual(str(s1), "[Square] (3) 5/10 - 4")

        s1.update(6, 7, 8, 9)
        self.assertEqual(str(s1), "[Square] (6) 8/9 - 7")

        s1.update(10, 11, 12, 13, 14)
        self.assertEqual(str(s1), "[Square] (10) 12/13 - 11")

    def test_update_validation_args(self):
        """Tests update *args validation.

            Validation is performed for all updated attributes except id.
        """

        s1 = Square(1, 2, 3, 4)

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               s1.update, None, None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               s1.update, 15, 0)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               s1.update, 15, 3, (1, 2))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               s1.update, 15, 3, -2)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               s1.update, 15, 3, 0, {"set", "set2"})
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               s1.update, 15, 3, 0, -4)

    def test_update_kwargs(self):
        """Tests the update method with **kwargs."""

        s1 = Square(10, 20, 30, 40)

        s1.update(id=None)
        expected = "[Square] ({}) 20/30 - 10".format(s1.id)
        self.assertEqual(str(s1), expected)

        s1.update(id=89, size=1)
        self.assertEqual(str(s1), "[Square] (89) 20/30 - 1")

        s1.update(id=90, size=10, x=5)
        self.assertEqual(str(s1), "[Square] (90) 5/30 - 10")

        s1.update(id=2, size=11, x=8, y=7)
        self.assertEqual(str(s1), "[Square] (2) 8/7 - 11")

    def test_update_validation_kwargs(self):
        """Tests update **kwargs validation.

            Validation is performed for all updated attributes except id.
        """

        s1 = Square(1, 2, 3, 4)

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               s1.update, size=None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               s1.update, id=90, size=0)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               s1.update, size=8, x=(1, 2))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               s1.update, x=-2)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               s1.update, y={"set", "set2"}, id=20)
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               s1.update, id=15, size=2, y=-3)

    def test_update_args_kwargs(self):
        """Tests the update method with *args and **kwargs.

            **kwargs is ignored if *args is provided.
        """
        s = Square(1, 2, 3, 4)

        s.update(10, 20, 30, id=90, size=40)
        self.assertEqual(str(s), "[Square] (10) 30/3 - 20")

    def test_update_kwargs_wrong_keys(self):
        """Tests the update method with the wrong keys for **kwargs."""

        s = Square(1, 2, 3, 4)

        s.update(h=1, w=2)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

        s.update(id=90, size=30, a=19, b=18)
        self.assertEqual(str(s), "[Square] (90) 2/3 - 30")


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests the to dictionary method."""

    def test_to_dictionary(self):
        """Test the to_dictionary method."""

        s1 = Square(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        expected = {"id": 9, "size": 10, "x": 2, "y": 1}
        self.assertDictEqual(s1_dict, expected)

        s1.update(10, 20, 30, 40)
        s1_dict = s1.to_dictionary()
        expected = {"id": 10, "size": 20, "x": 30, "y": 40}
        self.assertDictEqual(s1_dict, expected)

        s2 = Square(1, 1, 0, 0)
        s2_dict = s2.to_dictionary()
        expected = {"id": 0, "size": 1, "x": 1, "y": 0}
        self.assertDictEqual(s2_dict, expected)

    def test_to_dictionary_args(self):
        """Ensure type errors are raised for invalid number of arguments.

            to_dictionary takes no arguments.
        """
        s = Square(10)
        self.assertRaises(TypeError, s.to_dictionary, 1)


if __name__ == "__main__":
    unittest.main()
