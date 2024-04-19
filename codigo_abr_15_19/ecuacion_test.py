"""
Pruebas con la ecuación
"""

import unittest
from ecuacion import fEcu


class TestEcuacion(unittest.TestCase):

    def testExcepcion(self):
        self.assertRaises(ValueError, fEcu, 1, 2, 3)

    def testResultado(self):
        resul = fEcu(1, 5, 4)
        self.assertEqual(resul, (-1, -4), msg="No coincide el resultado")


if __name__ == "__main__":
    unittest.main()
