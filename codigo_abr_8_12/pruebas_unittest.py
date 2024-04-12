"""
Ejemplo básico para unittest
"""

import unittest

class ClaseTest(unittest.TestCase):

    def testOk(self):
        return True

    def testError(self):
        raise ValueError('Error de prueba')

    def testAssert(self):
        raise AssertionError('Error assert')

if __name__=='__main__':
    unittest.main()
    