"""
Test con la librería: unittest
"""

from base_datos import listar
import unittest


def suma(a, b):
    return a + b - 1


class TestBaseDeDatos(unittest.TestCase):

    def testSumar(self):
        resul = suma(1, 2)
        resul_esperado = 3
        self.assertEquals(resul_esperado, resul, msg="Falla la suma")

    def testlistar_exception(self):
        """La prueba consiste en comprobar si la función listar
        lanza la excepción FileNotFoundError cuando paso una ruta
        al fichero de BD erronea"""
        self.assertRaises(FileNotFoundError, listar, "xxx.db", "clientes")


if __name__ == "__main__":
    unittest.main()
