"""
Pruebas con la librería unittest
"""

import unittest


class Ejemplo(unittest.TestCase):

    def test2(self):
        self.assertAlmostEqual(
            3.456, 3.412, places=3, msg="No coinciden en los 3 primero decimales"
        )

    def testOk(self):
        pass

    def testException(self):
        raise ValueError("error de prueba")

    def testFail(self):
        raise AssertionError("Error assert")


if __name__ == "__main__":
    unittest.main()
