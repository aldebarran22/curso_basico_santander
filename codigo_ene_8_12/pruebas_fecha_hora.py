"""
Pruebas con PyUnit. Implementar una clase
que hereda de TestCase para chequear el modulo
fecha_hora.py
"""
import unittest
from fecha_hora import Time, TimeError


class PruebasTime(unittest.TestCase):
    def testStr(self):
        """
        Comprobar si al convertir en texto un Time hace correctamente
        el relleno de ceros
        """
        t1 = Time(2, 3, 1)
        self.assertEqual(str(t1), "02:03:01", msg="No rellena correctamente los ceros")

        t2 = Time(12)
        self.assertEqual(str(t2), "12:00:00", msg="No rellena correctamente los ceros")

    def testAdd(self):
        t1 = Time(2, 3, 1)
        t2 = Time(12)
        r = t1 + t2
        r2 = Time(14, 3, 1)
        self.assertEqual(str(r), str(r2), msg="No suma correctamente")

    def testException(self):
        pass


if __name__ == "__main__":
    unittest.main()
