"""
Chequear los ficheros generados por la función
exportar del módulo: bd_consultas.py
"""
from bd_consultas import exportar
import unittest
from os import remove
from os.path import isfile


class PruebasExportar(unittest.TestCase):
    def setUp(self):
        self.t = ("clientes", "pedidos")
        exportar("empresa3.db", *self.t)

    def testFicheros(self):
        for fich in self.t:
            path = f"../csv/{fich}.csv"
            self.assertTrue(isfile(path))

    def tearDown(self):
        # Borrar los ficheros:
        for f in self.t:
            path = f"../csv/{f}.csv"
            remove(path)


if __name__ == "__main__":
    unittest.main()
