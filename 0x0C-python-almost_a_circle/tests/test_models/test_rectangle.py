#!/usr/bin/python3
"""Rectangle class Test module"""
import unittest
import json
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout


class RectangleTest(unittest.TestCase):
    """Class to test rectangle module"""

    # testing initial values
    initial_ids = 0

    def setUp(self):
        """creates a Rectangle with the minum args"""
        self.rect_0 = Rectangle(1, 1)

    def test_00_is_base_class(self):
        """test if rectangle inherits from Base class"""
        self.assertTrue(issubclass(type(self.rect_0), Base)
                        and type(self.rect_0) != Base)

    def test_01_width_is_private(self):
        """test if the width property is private"""
        self.assertTrue('_Rectangle__width' in
                        dir(self.rect_0))

    def test_02_height_is_private(self):
        """test if the height property is private"""
        self.assertTrue('_Rectangle__height' in
                        dir(self.rect_0))

    def test_03_x_is_private(self):
        """test if the x property is private"""
        # with self.assertRaises(AttributeError):
        #     print(self.rect_0.x)
        self.assertTrue('_Rectangle__x' in
                        dir(self.rect_0))

    def test_04_y_is_private(self):
        """test if the height property is private"""
        self.assertTrue('_Rectangle__y' in
                        dir(self.rect_0))

    # testing id
    def test_0_no_args_Rectangle(self):
        """test Rectangle without args"""
        with self.assertRaises(TypeError):
            R1 = Rectangle()

    def test_1_1_args_Rectangle(self):
        """test Rectangle with just 1 arg"""
        with self.assertRaises(TypeError):
            R2 = Rectangle(1)

    def test_2_args_Rectangle(self):
        """test Rectangle two args witout id argument"""
        R3 = Rectangle(10, 2, 8, 2, 1)
        self.assertEqual(R3.id, 1)

    def test_3_args_Rectangle(self):
        """test Rectangle two args and id argument"""
        R4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(R4.id, 12)

    def test_4_args_Rectangle(self):
        """test Rectangle two args and repeat id argument"""
        R5 = Rectangle(10, 2, 0, 0, 2)
        self.assertEqual(R5.id, 2)

    # Starting to test width and height arguments
    def test_5_widthandheight_ok_Rectangle(self):
        """test Rectangle two testing width anf height"""
        R6 = Rectangle(10, 2, 0, 0, 2)
        self.assertEqual(R6.width, 10)
        self.assertEqual(R6.height, 2)
        self.assertEqual(R6.id, 2)

    def test_6_width_str_Rectangle(self):
        """test Rectangle TypeError width"""
        with self.assertRaises(TypeError):
            R7 = Rectangle("a", 10)

    def test_7_height_str_Rectangle(self):
        """test Rectangle TypeError heigth"""
        with self.assertRaises(TypeError):
            R8 = Rectangle(5, "10")

    def test_8_width_neg_Rectangle(self):
        """test Rectangle ValueError"""
        with self.assertRaises(ValueError):
            R9 = Rectangle(-5, 10)

    # Testing area
    def test_9_area_Rectangle(self):
        """test Rectangle area"""
        R10 = Rectangle(10, 2, 0, 0, 2)
        self.assertEqual(R10.area(), 20)

    def test_10_area_Rectangle(self):
        """test Rectangle area"""
        R11 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(R11.area(), 56)

    # Testing display
    def test_11_rectangle_display_1(self):
        """test the printing of a 3 * 2 rectangle"""
        R12 = Rectangle(3, 2)
        screen = io.StringIO()
        with redirect_stdout(screen):
            R12.display()
        self.assertEqual(screen.getvalue()[:-1], "###\n###")

    # Testing __str__
    def test_12_str_Rectangle(self):
        """ Testing method str"""
        R13 = Rectangle(4, 6, 2, 1, 12)
        str1 = "[Rectangle] (12) 2/1 - 4/6"
        str2 = R13.__str__()
        self.assertEqual(str2, str1)

    # Testing Display#1
    def test_13_Rectangle_display11(self):
        """ Testing display update """
        R14 = Rectangle(3, 2, 1, 0)
        screen = io.StringIO()
        with redirect_stdout(screen):
            R14.display()
        self.assertEqual(screen.getvalue()[:-1], " ###\n ###")

    # Testing Update
    def test_14_Rectangle_update_args(self):
        R15 = Rectangle(10, 10, 10, 10)
        R15.update(89)
        R15.update(89, 2)
        R15.update(89, 2, 3, 4, 5)
        str1 = R15.__str__()
        str2 = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str1, str2)

    # Testing Update #1, with keys
    def test_15_Rectangle_update_args_keys(self):
        R16 = Rectangle(10, 10, 10, 10)
        R16.update(height=1)
        R16.update(width=1, x=2)
        R16.update(y=1, width=2, x=3, id=89)
        R16.update(x=1, height=2, y=3, width=4)
        str1 = R16.__str__()
        str2 = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str1, str2)
