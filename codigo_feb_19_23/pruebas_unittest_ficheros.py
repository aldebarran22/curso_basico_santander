"""
Pruebas con unittest y el módulo de ficheros
"""

import unittest





class PruebasFicheros(unittest.TestCase):

    def setUp(self):
        self.num = 100
        print('Preparar contexto')

    def test(self):
        print(self.num)
        pass

    def tearDown(self):
        print('limpiar contexto')

    
   
if __name__ == "__main__":
    unittest.main()