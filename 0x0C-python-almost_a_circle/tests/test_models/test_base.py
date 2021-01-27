#!/usr/bin/python3
"""Base class Test module"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Class to test base module"""

    def test_0_id_no_arg(self):
        """Test none id"""
        A = Base()
        self.assertEqual(A.id, 1)

    def test_1_id_no_arg(self):
        """Test no arguments id 2"""
        B = Base()
        self.assertEqual(B.id, 2)

    def test_2_with_int_arg(self):
        """Test argument int"""
        B = Base(12)
        self.assertEqual(B.id, 12)

    def test_3_with_neg_arg(self):
        """Test argument negative"""
        B = Base(-112)
        self.assertEqual(B.id, -112)

    def test_4_with_neg_arg(self):
        """Default id. New instance without argument"""
        C = Base()
        self.assertEqual(C.id, 3)

    def test_5_more_arg(self):
        """test more arguments"""
        with self.assertRaises(TypeError):
            D = Base(0, 3)

    def test_6_with_char(self):
        """Test argument char"""
        E = Base('a')
        self.assertEqual(E.id, 'a')
