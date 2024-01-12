"""
Pruebas con PyUnit. Implementar una clase
que hereda de TestCase para chequear el modulo
fecha_hora.py
"""
import unittest
from fecha_hora import Time, TimeError


class PruebasTime(unittest.TestCase):
    def testStr(self):
        pass

    def testAdd(self):
        pass

    def testException(self):
        pass


if __name__ == "__main__":
    unittest.main()
