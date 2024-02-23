"""
Pruebas con unittest
"""

import unittest


class PruebasFicheros(unittest.TestCase):

    def test(self):
        pass

    def test2(self):
        raise AssertionError("error")

    def test3(self):
        raise ValueError("error 2")


if __name__ == "__main__":
    unittest.main()
