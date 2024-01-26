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
        path = "../ficheros_curso/Pedidos.txt"
        path2 = "../ficheros_curso"
        L = ["Alemania", "Francia", "Italia"]
        L.sort()
        ficheros.exportarPaises(path, *L)
        Lficheros = os.listdir(path2)
        Lficheros.sort()
        L2 = [f.partition(".")[0] for f in Lficheros]
        for f in L:
            if f not in L2:
                self.fail(f"No se encuentra un fichero para {f}")

        # self.assertEqual(L, L2, msg="No coinciden los ficheros con los países")


if __name__ == "__main__":
    unittest.main()
