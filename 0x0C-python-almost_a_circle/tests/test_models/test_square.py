#!/usr/bin/python3
"""Unittests for square.py"""
from io import StringIO
import unittest
import json
from unittest.mock import patch
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests the Square class."""

    def setUp(self):
        """Reset Base class private instance counter before each test."""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Test initializing of the square."""

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")

        s3 = Square(3, 1, 4)
        self.assertEqual(str(s3), "[Square] (3) 1/4 - 3")

        s4 = Square(9, 13, 20, 6)
        self.assertEqual(str(s4), "[Square] (6) 13/20 - 9")

    def test_validation(self):
        """Make sure errors are raised for invalid attributes."""

        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               Square, None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               Square, 0)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               Square, 10, "hello")
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               Square, 10, -4)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               Square, 10, 4, (1, 2))
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               Square, 10, 4, -3)

    def test_area(self):
        """Tests the area method."""

        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

        s2 = Square(8, 7, 0, 13)
        self.assertEqual(s2.area(), 64)

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
        s1 = Square(5)
        expected = "#####\n#####\n#####\n#####\n#####\n"
        self.assert_output(s1, expected)

        s2 = Square(3, 1, 2)
        expected = "\n\n ###\n ###\n ###\n"
        self.assert_output(s2, expected)

        s3 = Square(1, 1, 0, 13)
        expected = " #\n"
        self.assert_output(s3, expected)

    def test_update(self):
        """Tests the square update method."""

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(3, 4, 15)
        self.assertEqual(str(s1), "[Square] (3) 15/0 - 4")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(id=89, size=10)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 10")

        s1.update(1, 2, 3, x=12)
        self.assertEqual(str(s1), "[Square] (1) 3/1 - 2")

    def test_update_validation(self):
        """Make sure errors are raised for invalid updates."""
        s1 = Square(10)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertRaisesRegex(TypeError, "^width must be an integer$",
                               s1.update, None, None)
        self.assertRaisesRegex(ValueError, "^width must be > 0$",
                               s1.update, 15, 0)
        self.assertRaisesRegex(TypeError, "^x must be an integer$",
                               s1.update, x=(1, 2))
        self.assertRaisesRegex(ValueError, "^x must be >= 0$",
                               s1.update, 15, 3, -2)
        self.assertRaisesRegex(TypeError, "^y must be an integer$",
                               s1.update, 15, 3, 0, 2.5)
        self.assertRaisesRegex(ValueError, "^y must be >= 0$",
                               s1.update, y=-9)

    def test_to_dictionary(self):
        """Tests the to_dictionary method."""

        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s1_dict, expected)

        s2 = Square(15)
        s2_dict = s2.to_dictionary()
        expected = {"id": 2, "size": 15, "x": 0, "y": 0}
        self.assertEqual(s2_dict, expected)

        s3 = Square(19, 5, 4, 12)
        s3_dict = s3.to_dictionary()
        expected = {"id": 12, "size": 19, "x": 5, "y": 4}
        self.assertEqual(s3_dict, expected)

    def test_to_json_string(self):
        """Test the to_json_string Base class static method."""

        list_dicts = [{"id": 1, "size": 1, "x": 1, "y": 1}]
        expected = '[{"id": 1, "size": 1, "x": 1, "y": 1}]'
        self.assertEqual(Square.to_json_string(list_dicts), expected)

        list_dicts = None
        expected = "[]"
        self.assertEqual(Square.to_json_string(list_dicts), expected)

        list_dicts = []
        expected = "[]"
        self.assertEqual(Square.to_json_string(list_dicts), expected)

    def test_to_json_string_invalid_arguments(self):
        """Tests invalid arguments to the to_json_string method.

            to_json_string takes in one argument but no validation is performed
            to ensure that it is a list of dictionaries.So the behaviour in
            this case is undefined.
        """

        self.assertEqual(Square.to_json_string("hello"), '"hello"')
        self.assertEqual(Square.to_json_string((1, 2)), '[1, 2]')
        self.assertEqual(Square.to_json_string({"1": 1, "2": 2}),
                         '{"1": 1, "2": 2}')
        self.assertEqual(Square.to_json_string(1), '1')
        self.assertEqual(Square.to_json_string(2.5), '2.5')
        self.assertEqual(Square.to_json_string([1, 2, 3]), '[1, 2, 3]')
        self.assertEqual(Base.to_json_string(["h", "e", "f"]),
                         '["h", "e", "f"]')

        self.assertRaises(TypeError, Square.to_json_string, {1, 2, 3})
        self.assertRaises(TypeError, Square.to_json_string)

    def test_save_to_file(self):
        """Tests the save_to_file Base class method."""

        s1 = Square(10)
        s2 = Square(1, 2, 3, 9)
        Square.save_to_file([s1, s2])
        expected = ('[{"size": 10, "id": 1, "x": 0, "y": 0}, '
                    '{"size": 1, "x": 2, "y": 3, "id": 9}]')
        with open("Square.json", "r") as file:
            self.assertEqual(json.loads(file.read()), json.loads(expected))

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """Tests the from_json_string method."""
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 7, 'size': 7, 'x': 30, 'y': 40}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Square.from_json_string([]), [])
