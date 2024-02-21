"""
Herencia simple en Python
"""

from objetos import Persona


class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0.0, ambito="", idiomas=[]):
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre,edad,altura)
        self.ambito = ambito
        self.idiomas = idiomas


def testGuia():
    pass


if __name__ == "__main__":
    testGuia()
