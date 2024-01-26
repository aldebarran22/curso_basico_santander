"""
Pruebas con unittest.
"""

import unittest

class Pruebas1(unittest.TestCase):

    def test1(self):
        pass

    def test2(self):
        raise AssertionError('Fallo')
    
if __name__ == '__main__':
    unittest.main()