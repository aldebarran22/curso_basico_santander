"""
Chequear los ficheros generados por la función
exportar del módulo: bd_consultas.py
"""
from bd_consultas import exportar
import unittest


class PruebasExportar(unittest.TestCase):
    def test1(self):
        print("todo ok")

    def test2(self):
        raise Exception("error")


if __name__ == "__main__":
    unittest.main()
