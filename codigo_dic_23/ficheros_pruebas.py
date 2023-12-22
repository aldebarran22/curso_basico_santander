"""
Código de pruebas para el módulo ficheros.py
"""
import unittest
from ficheros import isFloat, leerEscribirFichero, leerFichero
from os import listdir


class PruebasFicheros(unittest.TestCase):
    def test_isFloat(self):
        self.assertFalse(isFloat("hola"), msg="La cadena la da como Float")
        self.assertTrue(isFloat("56.6"))

    def test_isFloat2(self):
        self.assertTrue(isFloat("12.34"), msg="No es un float")

    def test_ficheros_paises(self):
        paises = ["Finlandia", "Francia", "Alemania", "Suizas"]
        for p in paises:
            leerEscribirFichero("../ficheros/Pedidos.txt", p)
        ficheros = listdir("../ficheros")

        for p in paises:
            if p + ".csv" not in ficheros:
                AssertionError(f"No se ha generado el fichero para el pais: {p}")

    def test_leerFichero(self):
        self.assertRaises(FileNotFoundError, leerFichero, "hola.txt")


if __name__ == "__main__":
    unittest.main()
