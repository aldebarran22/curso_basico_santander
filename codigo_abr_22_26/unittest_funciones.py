"""
Estructura de un módulo para la generación de pruebas
con unittest
"""

import unittest

from ecuacion import calcularEcuacion

class TestFunciones(unittest.TestCase):

    def setUp(self):
        self.tupla = 1,5,4

    def test_resultado(self):
        resul = calcularEcuacion(*self.tupla)
        self.assertEqual(resul, (-1, -4), msg="No coincide el resultado")
        return True

    def test_exception(self):
        self.assertRaises(ValueError, calcularEcuacion, 1,2,3)
        
    def tearDown(self):
        del self.tupla

if __name__ == '__main__':
    unittest.main()