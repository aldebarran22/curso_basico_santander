"""
Pruebas con unittest y el módulo de ficheros
"""

import unittest


class PruebasFicheros(unittest.TestCase):

    def setUp(self):
        print('Preparar contexto')

    def test(self):
        pass

    def tearDown(self):
        print('limpiar contexto')

    
   
if __name__ == "__main__":
    unittest.main()