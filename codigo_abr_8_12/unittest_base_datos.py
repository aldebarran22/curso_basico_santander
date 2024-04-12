"""
Test de la base de datos
"""

import unittest
from base_datos_CRUD import ProductoCRUD

class TestEcuacion(unittest.TestCase):

    def testExcepcion(self):
        self.assertRaises(FileNotFoundError, ProductoCRUD, path="no existe.db")

if __name__=='__main__':
    unittest.main()