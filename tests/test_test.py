"""This is a file docstring"""

import unittest

def testable_func():
    """This function just returns a true value."""
    return False

class TestCaseCase(unittest.TestCase):
    """This is a class docstring."""

    def test_does_nothing(self):
        """This test asserts that the function returns true."""

        self.assertTrue(testable_func())
