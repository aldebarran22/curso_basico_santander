"""
Pruebas con unittest.
"""

import unittest
import ficheros
import os

class PruebasFicheros(unittest.TestCase):

    def testVariosPaises(self):
        """
        Exportar varios paises y comprobar si se genera un fichero
        por cada país
        """
        path = "../ficheros/Pedidos.txt"
        L = ["Alemania","Francia","Italia"]
        ficheros.exportarPaises(path, *L)
        Lficheros = os.listdir(path)
        L2 = [f.partition('.')[0] for f in Lficheros]
        self.assertEqual(L, L2, msg="No coinciden los ficheros con los países")


  
    
if __name__ == '__main__':
    unittest.main()