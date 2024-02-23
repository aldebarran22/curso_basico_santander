"""
Pruebas con unittest y el módulo de ficheros
"""

import unittest

from ficheros_paises import leerEscribirFichero
import os


class PruebasFicheros(unittest.TestCase):

    def setUp(self):
        f = open("../ficheros_curso/nombre_paises.txt", "r")
        txt = f.read()
        self.paises = txt.split("\n")
        f.close()

        for pais in self.paises:
            leerEscribirFichero("../ficheros_curso/Pedidos.csv", pais)

    def test(self):
        # Comprobar si hay un fichero por cada pais:
        L = os.listdir("../ficheros")
        self.assertEqual(
            len(self.paises),
            len(L),
            msg="No coinciden el número de ficheros con el número de paises",
        )

    def tearDown(self):
        # Eliminar todo los ficheros del contexto: carpeta "ficheros"
        for pais in self.paises:
            path = f"../ficheros/{pais}.csv"
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
