"""
Test de la base de datos
"""

import unittest
from base_datos_CRUD import ProductoCRUD, Producto, Categoria

class TestEcuacion(unittest.TestCase):

    def setUp(self):
        self.bd = ProductoCRUD('../bd/empresa3.db')
        

    def testRead(self):
        obj = self.bd.read(1)
        if obj.id != 1:
            self.fail("hay un error en el id")

    
    def testExcepcion(self):
        self.assertRaises(FileNotFoundError, ProductoCRUD, path="no existe.db")
    

    def tearDown(self):
        del self.bd

    

if __name__=='__main__':
    unittest.main()