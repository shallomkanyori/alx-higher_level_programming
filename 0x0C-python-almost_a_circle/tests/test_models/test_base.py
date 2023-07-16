#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_init(self):
        """Tests initializing.

            An id may be provided as an argument. If not or if the provided
            id is None, the private class attribute instance counter is
            incremented and the id of the instance is assigned to that value.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

        b5 = Base(None)
        self.assertEqual(b5.id, 4)

    def test_arguments(self):
        """Make sure type errors are raised for more than one arguments."""
        self.assertRaises(TypeError, Base, 1, 2)
        self.assertRaises(TypeError, Base, 1, 2, 3, 4, 5)

    def test_non_int_id(self):
        """Test non integer ids.

            The id is always assumed to be an integer but no validation is
            performed on the id provided.
        """
        b1 = Base("hello")
        self.assertEqual(b1.id, "hello")

        b2 = Base(12.5)
        self.assertEqual(b2.id, 12.5)

        b3 = Base([1, 2, 3])
        self.assertEqual(b3.id, [1, 2, 3])

        b4 = Base({"1": 1, "2": 2})
        self.assertEqual(b4.id, {"1": 1, "2": 2})
