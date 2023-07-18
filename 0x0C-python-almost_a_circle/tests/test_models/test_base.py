#!/usr/bin/python3
"""Unittests for base.py.

Unittest classes:
    TestBase_init - line 21
    TestBase_to_json_string - line 82
    TestBase_save_to_file - line 127
    TestBase_from_json_string - line 203
    TestBase_create - line 258
    TestBase_load_from_file - line 303
    TestBase_save_to_file_csv - line 357
    TestBase_load_from_file_csv - line 433
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """Unittests for the instantiation of the Base class."""

    def test_no_id(self):
        """Tests instantiation with no id provided"""

        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

        b3 = Base()
        self.assertEqual(b3.id, b1.id + 2)

    def test_none_id(self):
        """Test instantiation with id as None."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

        b3 = Base(None)
        self.assertEqual(b3.id, b1.id + 2)

    def test_with_id(self):
        """Tests instantiation with id provided"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_no_id_after_id(self):
        """Tests instantiation with no id provided after id provided."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_id_update(self):
        """Tests update to id."""
        b1 = Base(5)
        b1.id = 30
        self.assertEqual(b1.id, 30)

    def test_invalid_arguments(self):
        """Make sure type errors are raised for more than one arguments."""
        self.assertRaises(TypeError, Base, 1, 2)
        self.assertRaises(TypeError, Base, 1, 2, 3, 4, 5)

    def test_non_int_id(self):
        """Test non integer ids.

            The id is always assumed to be an integer but no validation is
            performed on the id provided.
        """
        self.assertEqual(Base("hello").id, "hello")
        self.assertEqual(Base(12.5).id, 12.5)
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base({"1": 1, "2": 2}).id, {"1": 1, "2": 2})
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})
        self.assertEqual(Base(False).id, False)
        self.assertEqual(Base(float("inf")).id, float("inf"))


class TestBase_to_json_string(unittest.TestCase):
    """Tests the to_json_string method."""

    def test_to_json_string_type(self):
        """Tests the return type of the to_json_string method."""
        r1 = Rectangle(10, 7, 2, 8, 9)
        self.assertEqual(type(Base.to_json_string([r1.to_dictionary()])), str)

        s1 = Square(10)
        self.assertEqual(type(Base.to_json_string([s1.to_dictionary()])), str)

    def test_to_json_string_rectangle(self):
        """Tests the to_json_string method on a list of rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 9)
        list_rects = [r1.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_rects)), 53)

        r2 = Rectangle(10, 10)
        list_rects.append(r2.to_dictionary())
        self.assertEqual(len(Base.to_json_string(list_rects)), 108)

    def test_to_json_string_square(self):
        """Tests the to_json_string method on a list of squares."""
        s1 = Square(5, 3, 4, 7)
        list_sq = [s1.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_sq)), 38)

        s2 = Square(3)
        list_sq.append(s2.to_dictionary())
        self.assertEqual(len(Base.to_json_string(list_sq)), 77)

    def test_to_json_string_empty(self):
        """Tests the to_json_string method on an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Tests the to_json_string method with None argument."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_invalid_args(self):
        """Make sure type errors are raised for < or > one argument."""
        self.assertRaises(TypeError, Base.to_json_string)
        self.assertRaises(TypeError, Base.to_json_string, [1, 2, 3], [])


class TestBase_save_to_file(unittest.TestCase):
    """Tests the save_to_file method."""

    def tearDown(self):
        """Delete any created files after each test."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_rectangle(self):
        """Tests the save_to_file method on a list of rectangles."""
        r1 = Rectangle(10, 7, 8, 2, 9)
        list_rects = [r1]
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 53)

        r2 = Rectangle(10, 20, 30)
        list_rects.append(r2)
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 109)

    def test_save_to_file_square(self):
        """Tests the save_to_file method on a list of squares."""
        s1 = Square(10, 20, 30, 40)
        list_sq = [s1]
        Square.save_to_file(list_sq)
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 42)

        s2 = Square(100)
        list_sq.append(s2)
        Square.save_to_file(list_sq)
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 83)

    def test_save_to_file_base(self):
        """Tests the save_to_file method on a list of base instances."""
        s1 = Square(10, 20, 30, 40)
        Base.save_to_file([s1])
        with open("Base.json", "r") as f:
            self.assertEqual(len(f.read()), 42)

    def test_save_to_file_overwrite(self):
        """Tests that the save_to_file method overwrites the file."""
        s1 = Square(10, 20, 30, 40)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 42)

        s2 = Square(100)
        Square.save_to_file([s2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 41)

    def test_save_to_file_none(self):
        """Test the save_to_file method with a None argument."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test the save_to_file method with an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_invalid_args(self):
        """Make sure type errors are raised for < or > one argument."""
        self.assertRaises(TypeError, Rectangle.save_to_file)
        self.assertRaises(TypeError, Rectangle.save_to_file, [1, 2, 3], [])


class TestBase_from_json_string(unittest.TestCase):
    """Tests the from_json_string method."""

    def test_from_json_string_type(self):
        """Tests the return type of the from_json_string method."""
        list_in = [{"id": 1, "width": 2, "height": 3}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(type(list_out), list)

    def test_from_json_string_rectangle(self):
        """Tests the from_json_string method with rectangles."""

        list_in = [{"id": 89, "width": 10, "height": 4}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_out, list_in)

        list_in = [
            {"id": 89, "width": 10, "height": 4},
            {"id": 7, "width": 1, "height": 7}
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_out, list_in)

    def test_from_json_string_square(self):
        """Tests the from_json_string method with squares."""

        list_in = [{"id": 89, "size": 30, "x": 1, "y": 2}]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_out, list_in)

        list_in = [
            {"id": 89, "size": 30, "x": 1, "y": 2},
            {"id": 90, "size": 10, "x": 12, "y": 5}
        ]
        json_list_in = Square.to_json_string(list_in)
        list_out = Square.from_json_string(json_list_in)
        self.assertEqual(list_out, list_in)

    def test_from_json_string_empty(self):
        """Tests the from_json_string method with an empty list string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Tests the from_json_string method with None argument."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_invalid_args(self):
        """Make sure type errors are raised for < or > one argument."""
        self.assertRaises(TypeError, Base.from_json_string)
        self.assertRaises(TypeError, Base.from_json_string, "[1, 2, 3]", "[]")


class TestBase_create(unittest.TestCase):
    """Tests the create method."""

    def test_create_rectangle(self):
        """Tests the create method with rectangles."""
        r1 = Rectangle(3, 5, 1, 10, 9)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] (9) 1/10 - 3/5")

    def test_create_rectagle_is(self):
        """Assert that the created rectangle is not the original rectangle."""
        r1 = Rectangle(3, 5, 1, 10, 9)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r2, r1)

    def test_create_rectagle_equals(self):
        """Assert that the new rectangle is not equal to the 1st rectangle."""
        r1 = Rectangle(3, 5, 1, 10, 9)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r2, r1)

    def test_create_square(self):
        """Tests the create method with squares."""
        s1 = Square(10, 20, 30, 40)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s2), "[Square] (40) 20/30 - 10")

    def test_create_square_is(self):
        """Assert that the created square is not the original square."""
        s1 = Square(10, 20, 30, 40)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s2, s1)

    def test_create_square_equals(self):
        """Assert that the new square is not equal to the 1st square."""
        s1 = Square(10, 20, 30, 40)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertNotEqual(s2, s1)


class TestBase_load_from_file(unittest.TestCase):
    """Tests the load_from_file method."""

    def tearDown(self):
        """Delete any created files after each test."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_rectangle(self):
        """Tests the load_to_file method with rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 10)
        r2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2])
        list_rects_out = Rectangle.load_from_file()
        self.assertEqual(str(list_rects_out[0]), str(r1))
        self.assertEqual(str(list_rects_out[1]), str(r2))

    def test_load_from_file_rectangle_type(self):
        """Tests the return type of the load_to_file method with rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 10)
        r2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1, r2])
        list_rects_out = Rectangle.load_from_file()
        self.assertTrue(all(type(r) is Rectangle for r in list_rects_out))

    def test_load_from_file_square(self):
        """Tests the load_from_file method with squares."""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        list_sq_out = Square.load_from_file()
        self.assertEqual(str(list_sq_out[0]), str(s1))
        self.assertEqual(str(list_sq_out[1]), str(s2))

    def test_load_from_file_square_type(self):
        """Tests the return type of the load_from_file method with square."""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file([s1, s2])
        list_sq_out = Square.load_from_file()
        self.assertTrue(all(type(s) is Square for s in list_sq_out))

    def test_load_from_file_no_file(self):
        """Tests the load_from_file method when the file doesn't exist."""
        list_rects_out = Rectangle.load_from_file()
        self.assertEqual(list_rects_out, [])

    def test_load_from_file_invalid_args(self):
        """Make sure type errors are raised with more than zero arguments."""
        self.assertRaises(TypeError, Square.load_from_file, "some_arg")


class TestBase_save_to_file_csv(unittest.TestCase):
    """Tests the save_to_file_csv method."""

    def tearDown(self):
        """Delete any created files after each test."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file__csv_rectangle(self):
        """Tests the save_to_file_csv method on a list of rectangles."""
        r1 = Rectangle(10, 7, 8, 2, 9)
        list_rects = [r1]
        Rectangle.save_to_file_csv(list_rects)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), "9,10,7,8,2\n")

        r2 = Rectangle(10, 20, 30, 40, 50)
        list_rects.append(r2)
        Rectangle.save_to_file_csv(list_rects)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), "9,10,7,8,2\n50,10,20,30,40\n")

    def test_save_to_file_csv_square(self):
        """Tests the save_to_file_csv method on a list of squares."""
        s1 = Square(10, 20, 30, 40)
        list_sq = [s1]
        Square.save_to_file_csv(list_sq)
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "40,10,20,30\n")

        s2 = Square(100, 2, 9, 7)
        list_sq.append(s2)
        Square.save_to_file_csv(list_sq)
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "40,10,20,30\n7,100,2,9\n")

    def test_save_to_file_csv_base(self):
        """Tests the save_to_file_csv method on a list of base instances."""
        s1 = Square(100, 2, 9, 7)
        Base.save_to_file_csv([s1])
        with open("Base.csv", "r") as f:
            self.assertEqual(f.read(), "7,100,2,9\n")

    def test_save_to_file_csv_overwrite(self):
        """Tests that the save_to_file_csv method overwrites the file."""
        s1 = Square(10, 20, 30, 40)
        Square.save_to_file_csv([s1])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "40,10,20,30\n")

        s2 = Square(100, 2, 9, 7)
        Square.save_to_file_csv([s2])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "7,100,2,9\n")

    def test_save_to_file_csv_none(self):
        """Test the save_to_file_csv method with a None argument."""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_csv_empty(self):
        """Test the save_to_file_csv method with an empty list."""
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_csv_invalid_args(self):
        """Make sure type errors are raised for < or > one argument."""
        self.assertRaises(TypeError, Rectangle.save_to_file_csv)
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, [1, 2, 3], [])


class TestBase_load_from_file_csv(unittest.TestCase):
    """Tests the load_from_file_csv method."""

    def tearDown(self):
        """Delete any created files after each test."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_rectangle(self):
        """Tests the load_to_file_csv method with rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 10)
        r2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r1, r2])
        list_rects_out = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rects_out[0]), str(r1))
        self.assertEqual(str(list_rects_out[1]), str(r2))

    def test_load_from_file_csv_rectangle_type(self):
        """Tests return type of the load_to_file_csv method with rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 10)
        r2 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r1, r2])
        list_rects_out = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(r) is Rectangle for r in list_rects_out))

    def test_load_from_file_csv_square(self):
        """Tests the load_from_file_csv method with squares."""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file_csv([s1, s2])
        list_sq_out = Square.load_from_file_csv()
        self.assertEqual(str(list_sq_out[0]), str(s1))
        self.assertEqual(str(list_sq_out[1]), str(s2))

    def test_load_from_file_csv_square_type(self):
        """Tests return type of the load_from_file_csv method with square."""
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6, 7, 8)
        Square.save_to_file_csv([s1, s2])
        list_sq_out = Square.load_from_file_csv()
        self.assertTrue(all(type(s) is Square for s in list_sq_out))

    def test_load_from_file_csv_no_file(self):
        """Tests the load_from_file_csv method when the file doesn't exist."""
        list_rects_out = Rectangle.load_from_file_csv()
        self.assertEqual(list_rects_out, [])

    def test_load_from_file_csv_invalid_args(self):
        """Make sure type errors are raised for < or > one argument."""
        self.assertRaises(TypeError, Square.load_from_file_csv, "some_arg")


if __name__ == "__main__":
    unittest.main()
