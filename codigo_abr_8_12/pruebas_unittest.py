"""
Ejemplo básico para unittest
"""

import unittest

class ClaseTest(unittest.TestCase):

    def testOk():
        return True

    def testError():
        raise ValueError('Error de prueba')

    def testAssert():
        raise AssertionError('Error assert')

if __name__=='__main__':
    unittest.main()
    