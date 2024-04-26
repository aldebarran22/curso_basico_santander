"""
Estructura de un módulo para la generación de pruebas
con unittest
"""

import unittest

from ecuacion import calcularEcuacion

class TestFunciones(unittest.TestCase):

    def test_resultado(self):
        resul = calcularEcuacion(1,5,4)
        self.assertEqual(resul, (-1, -4), msg="No coincide el resultado")
        return True

    def test_exception(self):
        self.assertRaises(ValueError, calcularEcuacion, 1,2,3)
        

if __name__ == '__main__':
    unittest.main()