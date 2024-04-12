"""
Comprobar si la función ecuación funciona correctamente.
"""

import funciones_curso
import unittest

class TestEcuacion(unittest.TestCase):

    def testExcepcion(self):
        self.assertRaises(ValueError, funciones_curso.ecuacion, 1,2,3)

    def testResultado(self):
        resul = funciones_curso.ecuacion(1,5,4)
        self.assertEqual(resul, (-1, -4), msg="No coincide el resultado de la ecu.")


if __name__=='__main__':
    unittest.main()