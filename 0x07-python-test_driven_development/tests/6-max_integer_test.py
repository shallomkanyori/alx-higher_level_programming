#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function."""
    def test_sequences(self):
        """Tests max integer for sequence types."""
        self.assertEqual(max_integer([1, 2, 2.5, 3, 4]), 4)
        self.assertEqual(max_integer((-4, 14, 20, 88, -90)), 88)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer("hello"), 'o')
        self.assertEqual(max_integer(b"hello"), 111)
        self.assertEqual(max_integer(range(-10, 0, 2)), -2)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_non_sequences(self):
        """Make sure type errors are raised for non-sequence types."""
        self.assertRaises(TypeError, max_integer, {1, 2, 3, 4})
        self.assertRaises(TypeError, max_integer, 12)
        self.assertRaises(TypeError, max_integer, 19.89)
        self.assertRaises(TypeError, max_integer, None)

    def test_mixed_sequences(self):
        """"Make sure type errors are raised for sequences with mixed types.

            Type errors should be raised for sequences that contain non-numeric
            mixed types."""
        self.assertRaises(TypeError, max_integer, [1, "2", 3, 4])
        self.assertRaises(TypeError, max_integer, ((1, 2), -10, 31))
        self.assertRaises(TypeError, max_integer, [1, 2, (3, 4)])

    def test_non_comparable_sequences(self):
        """Make sure type errors are raised for sequences of non-comparable
        types.

            Type errors should be raised for sequences that contain
            non-comparable types."""
        self.assertRaises(TypeError, max_integer, [{"1": 1, "2": 2}, {"4": 4}])
        self.assertRaises(TypeError, max_integer, (None, None, None))
