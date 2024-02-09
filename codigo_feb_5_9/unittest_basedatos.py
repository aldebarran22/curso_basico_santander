"""
Pruebas sobre el módulo: basedatosCRUD.
"""

import unittest
from basedatosCRUD import BaseDatos


class PruebaBD(unittest.TestCase):

    def test_exceptions(self):
        # Comprobar si lanza una exception cuando
        # está mal la ruta de la BD
        self.assertRaises(FileNotFoundError, BaseDatos, "no existe.db")

    def test_delete(self):
        bd = BaseDatos("../bd/empresa3.db")
        obj = bd.read(8)
        bd.delete(8)
        self.assertRaises(ValueError, bd.read, 8)


if __name__ == "__main__":
    unittest.main()
