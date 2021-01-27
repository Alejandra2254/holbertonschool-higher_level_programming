"""Test Square Module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io


class testSquare(unittest.TestCase):
    """Rectangle test class"""

    initial_ids = 0

    def check_initial_ids(self):
        """checks if there are ids already initialized"""
        if '_Base__nb_objects' in dir(Square):
            type(self).initial_ids = Square.__dict__['_Base__nb_objects'] - 1

    def setUp(self):
        """creates a Rectangle with the minum args"""
        self.S0 = Square(2)

    def test_0_is_Rectangle_class(self):
        """test if square inherits from Rectangle class"""
        self.assertTrue(issubclass(type(self.S0), Rectangle) and
                        type(self.S0) != Rectangle)

    def test_1_square_attributes(self):
        """test the correct creation of the attributes of the new instance
           with default arguments
        """
        self.assertEqual(self.S0.width, 2)
        self.assertEqual(self.S0.height, 2)
        self.assertEqual(self.S0.x, 0)
        self.assertEqual(self.S0.y, 0)

    # testing id
    def test_2_no_args_square(self):
        """test Rectangle without args"""
        with self.assertRaises(TypeError):
            S1 = Square()

    def test_3_square_attributes_with_args(self):
        """test the correct creation of the attributes of the new instance
           with custom arguments
        """
        S2 = Square(4, 1, 2, -5)
        self.assertEqual(S2.width, 4)
        self.assertEqual(S2.height, 4)
        self.assertEqual(S2.x, 1)
        self.assertEqual(S2.y, 2)
        self.assertEqual(S2.id, -5)

    def test_4_size_integer(self):
        """test if size is integer"""
        with self.assertRaises(TypeError):
            S3 = Square('a')

    def test_5_size_less_than_1(self):
        """test if size is less than 1"""
        with self.assertRaises(ValueError):
            S4 = Square(0)

    def test_6_x_integer(self):
        """test if x is integer"""
        with self.assertRaises(TypeError):
            S5 = Square(1, 'a')
