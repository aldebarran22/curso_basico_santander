"""
Pruebas con unittest
"""

import unittest
from funciones_curso import ecuacion


class TestEcuacion(unittest.TestCase):

    def testOk(self):
        resul = ecuacion(1, 5, 4)
        t = (-1, -4)
        self.assertEqual(resul, t, msg="No coincide el resultado esperado.")

    def testError(self):
        self.assertRaises(ValueError, ecuacion, 1, 2, 3)


if __name__ == "__main__":
    unittest.main()
