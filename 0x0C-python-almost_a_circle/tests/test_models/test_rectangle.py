#!/usr/bin/python3
"""Unittests for rectangle.py."""
import unittest
import json
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class."""

    def setUp(self):
        """Reset the Base class private attribute instance counter."""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Tests initialization of a rectangle."""

        r1 = Rectangle(10, 2)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 10/2")

        r2 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r2), "[Rectangle] (12) 2/1 - 4/6")

        r3 = Rectangle(5, 5, 1)
        self.assertEqual(str(r3), "[Rectangle] (2) 1/0 - 5/5")

    def test_validation_integer(self):
        """Make sure type errors are raised for non-integer attributes.

            This does not apply to the id attribute.
        """

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Rectangle, "10", 2)
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               Rectangle, 10, 2.5)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Rectangle, 10, 2, None)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 10, 2, 1, (1, 2))
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Rectangle, 10, 2, 1, {1, 2, 3})

    def test_validation_positive(self):
        """Make sure value errors are raised for non-positive attributes.

            For width and height attributes, 0 is considered non positive.
            For x and y attributes, 0 is considered positive.
            This does not apply to the id attribute.
        """

        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Rectangle, -10, 2)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Rectangle, 0, 2)
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               Rectangle, 10, -2)
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               Rectangle, 10, 0)
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               Rectangle, 10, 2, -1, 0)
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               Rectangle, 10, 2, 0, -5)

    def test_area(self):
        """Tests the area method."""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

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

    def test_update_args(self):
        """Tests the update method with *args only."""

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(99, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (99) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Tests the update method with **kwargs.

            If both *args and *kwargs are provided, **kwargs are ignored."""

        r1 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(str(r1), "[Rectangle] (50) 30/40 - 10/20")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (50) 30/40 - 10/1")

        r1.update(x=1, y=19, height=2, width=4, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/19 - 4/2")

        r1.update(10, 20, 30, x=15, y=1)
        self.assertEqual(str(r1), "[Rectangle] (10) 1/19 - 20/30")

    def test_update_validation(self):
        """Validation is performed for all updated attributes except id."""

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               r1.update, None, None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               r1.update, 15, 0)
        self.assertRaisesRegex(TypeError, "^height must be an integer$",
                               r1.update, height="hello")
        self.assertRaisesRegex(ValueError, "^height must be > 0$",
                               r1.update, 15, 3, -5)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               r1.update, x=(1, 2))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               r1.update, 15, 3, 8, -2)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               r1.update, 15, 3, 8, 0, {"set", "set2"})
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               r1.update, id=15, height=2, y=-3)

    def test_update_arguments(self):
        """Make sure errors are raised for incorrect arguments to update."""

        r1 = Rectangle(1, 2)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/2")

        self.assertRaises(IndexError, r1.update, 1, 2, 3, 4, 5, 6)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r1_dict, expected)

        r1.update(10, 20, 30, 40)
        r1_dict = r1.to_dictionary()
        expected = {"id": 10, "width": 20, "height": 30, "x": 40, "y": 9}
        self.assertEqual(r1_dict, expected)

        r2 = Rectangle(1, 1)
        r2_dict = r2.to_dictionary()
        expected = {"id": 2, "width": 1, "height": 1, "x": 0, "y": 0}
        self.assertEqual(r2_dict, expected)

    def test_save_to_file(self):
        """Tests the save_to_file class method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        expected = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, '
                    '{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), json.loads(expected))

        r1.update(height=15, y=2)
        r2.update(1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        expected = ('[{"y": 2, "x": 2, "id": 1, "width": 10, "height": 15}, '
                    '{"y": 0, "x": 0, "id": 1, "width": 2, "height": 3}]')
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), json.loads(expected))

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """Tests the from_json_string method."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string([]), [])
