"""
Pruebas con unittest y el módulo de ficheros
"""

import unittest

from ficheros_paises import leerEscribirFichero


class PruebasFicheros(unittest.TestCase):

    def setUp(self):
        f = open("../ficheros_curso/nombre_paises.txt", "r")
        txt = f.read()
        self.paises = txt.split("\n")
        f.close()

    def test(self):
        print(self.paises)

    def tearDown(self):
        print("limpiar contexto")


if __name__ == "__main__":
    unittest.main()
