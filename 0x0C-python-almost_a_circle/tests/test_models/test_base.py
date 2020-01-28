#!/usr/bin/python3
""" Test_Base """
import unittest
from models.rectangle import Rectangle
from models.square import Square
import sys
import io


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

    def test_rec_7(self):
        """ Display tests """
        r = Rectangle(2, 3, 2, 2)
        out = self.capture_stdout(r, "display")
        self.assertEqual("\n\n  ##\n  ##\n  ##\n", out.getvalue())
        r = Rectangle(3, 2, 1, 0)
        out = self.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", out.getvalue())
        r = Rectangle(5, 5, 5, 5)
        out = self.capture_stdout(r, "display")
        correct = "\n\n\n\n\n     #####\n     #####\n     #####\n"
        correct += "     #####\n     #####\n"
        self.assertEqual(correct, out.getvalue())

    def test_rec_8(self):
        """ Str tests """
        r = Rectangle (2, 2, 2, 2)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (7) 2/2 - 2/2\n", out.getvalue())
        r = Rectangle (3, 1, 2, 4)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (8) 2/4 - 3/1\n", out.getvalue())

    def test_rec_9(self):
        """ Update tests """
        r = Rectangle (10, 10, 10, 10)
        r.update(89)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10\n", out.getvalue())
        r.update(89, 2)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10\n", out.getvalue())
        r.update(89, 2, 3)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3\n", out.getvalue())
        r.update(89, 2, 3, 4)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3\n", out.getvalue())
        r.update(89, 2, 3, 4, 5)
        out = self.capture_stdout(r, "print")
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3\n", out.getvalue())

    @staticmethod
    def capture_stdout(obj, method):
        """ return the stdoutput """
        ioValue = io.StringIO()
        sys.stdout = ioValue
        if method == "print":
            print(obj)
        else:
            obj.display()
        sys.stdout = sys.__stdout__
        return ioValue
