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

    def test_to_json_string(self):
        """Test the to_json_string method."""

        list_dicts = [{"id": 1, "width": 1, "height": 1, "x": 1, "y": 1}]
        expected = '[{"id": 1, "width": 1, "height": 1, "x": 1, "y": 1}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected)

        list_dicts = None
        expected = "[]"
        self.assertEqual(Base.to_json_string(list_dicts), expected)

        list_dicts = []
        expected = "[]"
        self.assertEqual(Base.to_json_string(list_dicts), expected)

    def test_to_json_string_invalid_arguments(self):
        """Tests invalid arguments to the to_json_string method.

            to_json_string takes in one argument but no validation is performed
            to ensure that it is a list of dictionaries.So the behaviour in
            this case is undefined.
        """

        self.assertEqual(Base.to_json_string("hello"), '"hello"')
        self.assertEqual(Base.to_json_string((1, 2)), '[1, 2]')
        self.assertEqual(Base.to_json_string({"1": 1, "2": 2}),
                         '{"1": 1, "2": 2}')
        self.assertEqual(Base.to_json_string(1), '1')
        self.assertEqual(Base.to_json_string(2.5), '2.5')
        self.assertEqual(Base.to_json_string([1, 2, 3]), '[1, 2, 3]')
        self.assertEqual(Base.to_json_string(["h", "e", "f"]),
                         '["h", "e", "f"]')

        self.assertRaises(TypeError, Base.to_json_string, {1, 2, 3})
        self.assertRaises(TypeError, Base.to_json_string)
