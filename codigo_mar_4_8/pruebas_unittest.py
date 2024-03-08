"""
Ejemplo de pruebas con unittest
"""

import unittest
from ficheros_empleados import fusion
from ecugrado2 import ecuacion
from os import remove


class PruebasEcu(unittest.TestCase):

    def testEcuacionExc(self):
        self.assertRaises(ValueError, ecuacion, 1, 2, 3)

    def testEcuacionOk(self):
        resul = ecuacion(1, 5, 4)
        self.assertEqual((-4, -1), resul, msg="No coincide con el resul esperado")


class PruebasFunciones(unittest.TestCase):

    def setUp(self):
        print("Generando la fusión de ficheros")
        path1 = "../ficheros_curso/Empleados2.txt"
        path2 = "../ficheros_curso/Empleados3.txt"
        pathDestino = "../ficheros/empleados.csv"

        fusion(path1, path2, pathDestino)

    def test_fusion_ficheros(self):
        pathDestino = "../ficheros/empleados.csv"
        pathMaestro = "../ficheros_curso/empleados_maestro.csv"
        f1 = open(pathDestino, "r")
        f2 = open(pathMaestro, "r")
        txt1 = f1.read()
        txt2 = f2.read()
        self.assertEqual(
            txt1, txt2, msg="No coincide el fichero maestro con el fichero generado"
        )
        f1.close()
        f2.close()

    def tearDown(self):
        # Borrar el fichero generado
        pathDestino = "../ficheros/empleados.csv"
        remove(pathDestino)


if __name__ == "__main__":
    unittest.main()
