"""
Ejemplo de pruebas con unittest
"""

import unittest
from ficheros_empleados import fusion


class Pruebas(unittest.TestCase):

    def test_1(self):
        path1 = "../ficheros_curso/Empleados2.txt"
        path2 = "../ficheros_curso/Empleados3.txt"
        pathDestino = "../ficheros/empleados.csv"

        fusion(path1, path2, pathDestino)
        pathMaestro = "../ficheros_curso/empleados_maestro.csv"


if __name__ == "__main__":
    unittest.main()
