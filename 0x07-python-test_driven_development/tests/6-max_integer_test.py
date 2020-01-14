#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Check a list in order
        m_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_integer(m_list), 6)
        # Check a list non order
        m_list = [5, 6, 5, 1, 3, 2]
        self.assertEqual(max_integer(m_list), 6)
        # Check without parameter
        self.assertEqual(max_integer(), None)
        # Check an empty list
        self.assertEqual(max_integer([]), None)
        # Check if TypeError is raised
        with self.assertRaises(TypeError):
            max_integer(["Hello"])
        

if __name__ == '__main__':
    unittest.main()