#!/usr/bin/python3

"""Unittest for max_integer([..])."""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This class regroups test for the function max_integer()."""

    def test_valid_list(self):
        """Test if max_integer works with a valid list."""
        test_list = [1, 2, 3]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(3, max_num)

    def test_empty_list(self):
        """Test if max_integer works with an empty list."""
        test_list = []
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(None, max_num)

    def test_float_list(self):
        """Test if max_integer works with a float list."""
        test_list = [1.1, 2.2, 3.3]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(3.3, max_num)

    def test_negative_integer_list(self):
        """Test if max_integer works with negative numbers."""
        test_list = [-1, -2, -3]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(-1, max_num)

    def test_single_number_integer_list(self):
        """Test if max_integer works with a number."""
        test_list = [100]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(100, max_num)

    def test_same_numbers_integer_list(self):
        """Test if max_integer works with same numbers."""
        test_list = [100, 100, 100]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(100, max_num)

    def test_float_integer_list(self):
        """Test if max_integer works with float and integer."""
        test_list = [-1000, 0, 6.2]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(6.2, max_num)

    def test_big_list(self):
        """Test if max_integer works with a number."""
        test_list = [
            100,
            9,
            9000000000,
            6.43344,
            -766666666768,
            -465465.7876,
            687678687687646,
            0,
            12,
            -576576,
            676,
            0,
        ]
        # Call max_integer
        max_num = max_integer(test_list)
        self.assertEqual(687678687687646, max_num)


if __name__ == "__main__":
    unittest.main()
