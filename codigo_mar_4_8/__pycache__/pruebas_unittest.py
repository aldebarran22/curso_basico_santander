"""
Ejemplo de pruebas con unittest
"""

import unittest

class Pruebas(unittest.TestCase):

    def test_1(self):
        return True
    
    def test_2(self):
        raise ValueError('un error')
    
    def test_3(self):
        raise AssertionError('error 2')
    
if __name__ == '__main__':
    unittest.main()