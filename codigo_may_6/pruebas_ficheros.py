"""
Ejecución de pruebas con unittestt

Comprobar la generación de ficheros de pedidos
"""

import unittest

from ficheros_paises import leerEscribirFichero


class Pruebas(unittest.TestCase):

    L = ["Francia", "Estados Unidos", "Finlandia", "Suiza"]

    def setUp(self):
        pass

    def test_paises(self):
        return True

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
