"""
Estructura de un módulo para la generación de pruebas
con unittest
"""

import unittest

class TestEjemplo1(unittest.TestCase):

    def test_ok(self):
        return True

    def test_exception(self):
        raise ValueError('Error general')

    def test_assertion(self):
        raise AssertionError("Assert error")

if __name__ == '__main__':
    unittest.main()