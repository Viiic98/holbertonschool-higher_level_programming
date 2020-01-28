#!/usr/bin/python3
""" Test_Base """
import unittest
from models.rectangle import Rectangle
from models.square import Square


class Base_Test(unittest.TestCase):
    """ Class that test all """

    def test_rec_0(self):
        """ Raise type error """
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_rec_1(self):
        """ Raise type error """
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rec_2(self):
        """ Raise value error """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_rec_3(self):
        """ Raise value error """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_rec_4(self):
        """ Raise value error """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -1, 1)

    def test_rec_5(self):
        """ Raise value error """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 1, -1)

    def test_rec_6(self):
        """ Area tests """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)
        r = Rectangle(9, 8)
        self.assertEqual(r.area(), 72)
