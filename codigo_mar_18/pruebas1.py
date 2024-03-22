"""
Ejemplo de pruebas con unittest
"""

import unittest


class EjemploPruebas(unittest.TestCase):

    def testok(self):
        return False

    def testFails(self):
        raise AssertionError("Fail")

    def testException(self):
        raise Exception("Error")


if __name__ == "__main__":
    unittest.main()
