"""
Ejemplo de pruebas con unittest
"""

import unittest
from ficheros_empleados import fusion
from ecugrado2 import ecuacion


class PruebasFunciones(unittest.TestCase):

    def testEcuacionExc(self):
        self.assertRaises(ValueError, ecuacion, 1, 2, 3)

    def testEcuacionOk(self):
        resul = ecuacion(1, 5, 4)
        self.assertEqual((-4, -1), resul, msg="No coincide con el resul esperado")

    def te_st_fusion_ficheros(self):
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
