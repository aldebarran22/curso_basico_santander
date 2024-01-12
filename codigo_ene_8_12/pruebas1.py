"""
Pruebas con PyUnit. Implementar una clase
que hereda de TestCase. 
"""
import unittest


class Pruebas1(unittest.TestCase):
    def test1(self):
        print("todo ok")

    def test2(self):
        raise Exception("error")


if __name__ == "__main__":
    unittest.main()
