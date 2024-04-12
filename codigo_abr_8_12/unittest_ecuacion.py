"""
Comprobar si la función ecuación funciona correctamente.
"""

from funciones_curso import ecuacion
import unittest

class TestEcuacion(unittest.TestCase):

    def testExcepcion(self):
        pass

    def testResultado(self):
        resul = ecuacion(1,5,4)
        self.assertEqual(resul, (-1, -5), msg="No coincide el resultado de la ecu.")


if __name__=='__main__':
    unittest.main()