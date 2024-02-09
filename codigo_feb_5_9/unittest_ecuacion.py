"""
Esquema para hacer pruebas del software
con la librería unittest.
"""

import unittest
from ecuacion import ecuGrado2


class Pruebas1(unittest.TestCase):

    def testEcuacionOK(self):
        resultado = ecuGrado2(1, 5, 4)
        t = (-1, -4)
        self.assertEqual(
            resultado, t, msg="No coincide el resultado para a=1, b=5, c=4"
        )

    def testEcuacionError(self):
        self.assertRaises(ValueError, ecuGrado2, 1, 2, 3)


if __name__ == "__main__":
    unittest.main()
