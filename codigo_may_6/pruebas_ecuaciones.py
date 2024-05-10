"""
Pruebas con unittest para chequear la ecuacion
"""

import unittest
from ecuaciones_funcion import ecuacion


class Pruebas(unittest.TestCase):

    def setUp(self):
        print("inicio contexto")

    def tearDown(self):
        print("fin contexto")

    def test_ok(self):
        """Comprobar si un resultado es correcto"""
        resul = ecuacion(1, 5, 4)
        self.assertEqual(resul, (-1, -4), msg="Cálculo incorrecto")

    def test_excepcion(self):
        """Comprobar si lanza una excepción cuando no tiene solución"""
        self.assertRaises(ValueError, ecuacion, 1, 2, 3)

    def test_assert(self):
        pass


if __name__ == "__main__":
    unittest.main()
