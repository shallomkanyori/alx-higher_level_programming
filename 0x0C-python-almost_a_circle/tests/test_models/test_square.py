#!/usr/bin/python3
"""Unittests for square.py"""
import unittest
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
