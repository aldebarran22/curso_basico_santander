"""
Ejecución de pruebas con unittestt
"""

import unittest


class Pruebas(unittest.TestCase):

    def test_ok(self):
        return True

    def test_error(self):
        raise Exception("Se produce un error")

    def test_assert(self):
        raise AssertionError("Error en assert")


if __name__ == "__main__":
    unittest.main()
