"""
POO en Python
"""

from random import randint
from string import ascii_uppercase


def generarDatos():
    candidatos = [
        {
            "nombre": letra * 3,
            "años": randint(5, 10),
            "numempresas": randint(1, 8),
            "superior": True if randint(2, 10) % 2 == 0 else False,
        }
        for letra in ascii_uppercase
    ]
    return candidatos


class Candidato:
    """Implementación de la clase Candidato"""

    def __init__(self, nombre="", años=0, numempresas=0, superior=False):
        # Definir atributos:
        self.nombre = nombre
        self.años = años
        self.numempresas = numempresas
        self.superior = superior

    def actualizarExp(self):
        self.años += 1

    def __str__(self):
        return (
            self.nombre
            + " "
            + str(self.años)
            + " "
            + str(self.numempresas)
            + " "
            + str(self.superior)
        )


if __name__ == "__main__":
    c1 = Candidato("Juan", 10, 5, True)
    print(c1)
    c1.actualizarExp()
    print(c1)
    # print(str(c1))
    # print(c1.__str__())
