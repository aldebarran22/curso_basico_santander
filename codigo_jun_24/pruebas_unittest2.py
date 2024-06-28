"""
Pruebas con la librería unittest
"""

import unittest
from base_datos_CRUD import Empleado, EmpleadoCRUD

class Ejemplo(unittest.TestCase):

    def testFile(self):
        self.assertRaises(FileNotFoundError, EmpleadoCRUD, "empresa3.db")        
   

if __name__ == "__main__":
    unittest.main()
