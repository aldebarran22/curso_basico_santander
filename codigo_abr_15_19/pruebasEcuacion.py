"""
Pruebas del SW
"""

import unittest


class TestEjemplo(unittest.TestCase):

    def testok(self):
        return True

    def testFail(self):
        raise AssertionError("assert error")

    def testException(self):
        raise ValueError("ValueError")


if __name__ == "__main__":
    unittest.main()
