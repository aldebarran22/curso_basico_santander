"""
Chequear los ficheros generados por la función
exportar del módulo: bd_consultas.py
"""
from bd_consultas import exportar
import unittest
from os import remove


class PruebasExportar(unittest.TestCase):

    def setUp(self):
        self.t = ("clientes", "pedidos")
        exportar("empresa3.db", *self.t)

    def testFicheros(self):
        pass

    def tearDown(self):
        # Borrar los ficheros:
        for f in self.t:
            path = "../csv/{f}.csv"
            remove(path)



if __name__ == "__main__":
    unittest.main()
