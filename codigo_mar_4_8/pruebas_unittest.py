"""
Ejemplo de pruebas con unittest
"""

import unittest
from ficheros_empleados import fusion


class PruebasFunciones(unittest.TestCase):

    def test_fusion_ficheros(self):
        path1 = "../ficheros_curso/Empleados2.txt"
        path2 = "../ficheros_curso/Empleados3.txt"
        pathDestino = "../ficheros/empleados.csv"

        fusion(path1, path2, pathDestino)
        pathMaestro = "../ficheros_curso/empleados_maestro.csv"
        f1 = open(pathDestino, "r")
        f2 = open(pathMaestro, "r")
        txt1 = f1.read()
        txt2 = f2.read()
        self.assertEqual(
            txt1, txt2, msg="No coincide el fichero maestro con el fichero generado"
        )


if __name__ == "__main__":
    unittest.main()
