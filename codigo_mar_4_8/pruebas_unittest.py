"""
Ejemplo de pruebas con unittest
"""

import unittest
from ficheros_empleados import fusion


class Pruebas(unittest.TestCase):

    def test_1(self):
        "../ficheros_curso/Empleados2.txt"
        "../ficheros_curso/Empleados3.txt"
        "../ficheros/empleados.csv"
        return True

    def test_2(self):
        raise ValueError("un error")

    def test_3(self):
        raise AssertionError("error 2")


if __name__ == "__main__":
    unittest.main()
