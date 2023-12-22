"""
Código de pruebas para el módulo ficheros.py
"""
import unittest
from ficheros import isFloat


class PruebasFicheros(unittest.TestCase):
    def test_isFloat(self):
        self.assertFalse(isFloat("hola"), msg="La cadena la da como Float")
        self.assertTrue(isFloat("56.6"))


if __name__ == "__main__":
    unittest.main()
