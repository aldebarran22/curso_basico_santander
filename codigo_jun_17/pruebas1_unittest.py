"""
Ejemplo básico del funcionamiento de la librería unittest
La clase tiene 3 métodos:
1- todo ok
2- Lanzar AssertionError
3- Lanzar una excepción
"""

import unittest

class Pruebas(unittest.TestCase):

    def testOk(self):
        print("resultado")

    def testAssert(self):
        raise AssertionError("Error de assert")

    def testException(self):
        raise ValueError("Se produce ValueError")

if __name__ == '__main__':
    unittest.main()