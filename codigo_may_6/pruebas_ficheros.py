"""
Ejecución de pruebas con unittestt

Comprobar la generación de ficheros de pedidos
"""

import unittest

from ficheros_paises import leerEscribirFichero

from os import listdir, remove


class Pruebas(unittest.TestCase):

    L = ["Francia", "Estados Unidos", "Finlandia", "Suiza"]

    def setUp(self):
        for pais in Pruebas.L:
            leerEscribirFichero("../ficheros_curso/pedidos.csv", pais)

    def test_paises(self):
        """Comprobar si el numero de ficheros coincide con la lista"""
        self.lista = listdir("../ficheros")
        self.assertEqual(
            len(self.lista), len(Pruebas.L), msg="No coincide el número de ficheros"
        )

    def tearDown(self):
        """Borrar todos los ficheros generados en el contexto"""
        for path in self.lista:
            remove(path)


if __name__ == "__main__":
    unittest.main()
