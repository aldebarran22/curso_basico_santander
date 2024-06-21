"""
Implementar una clase de pruebas para las funciones del curso
y la clase ProductoCRUD
- Para la ecuación 2 pruebas: 
a) Con el resultado correcto
b) Con unos coeficientes que no tienen solución (chequear la excepcion)
"""

import unittest

from funciones_curso import ecuacion

class Pruebas(unittest.TestCase):

    def testEcuacion(self):
        """
        Comprobar si el resultado de la ecuación es correcto.        
        """
        resul = ecuacion(1,5,4)
        self.assertEqual((-1,-4), resul, msg="No coincide el resultado")

    def testEcuacionExcept(self):
        pass

   

if __name__ == '__main__':
    unittest.main()