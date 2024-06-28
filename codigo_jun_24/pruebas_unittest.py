"""
Pruebas con la librería unittest
"""

import unittest

class Ejemplo(unittest.TestCase):

    def testOk(self):
        pass

    def testException(self):
        raise ValueError("error de prueba")
    
    def testFail(self):
        raise AssertionError("Error assert")
    

if __name__ == '__main__':
    unittest.main()