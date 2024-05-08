"""
POO en Python:
Diseño de clases
- Sobrecarga de operadores
- Funciones especiales 
- Listas de objetos
"""


from typing import Any


class Persona:
    """Implementación de la clase Persona"""

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + str(self.altura) + " " + str(self.edad)

    def __repr__(self):
        return str(self)

    def __del__(self):
        pass
        # print('Se está borrando: ', self.nombre)


def pruebaPersona():
    p1 = Persona("Miguel", 34, 1.8)
    p2 = Persona("Eva", 44, 1.79)
    print(p1)
    # print(str(p1))
    # print(p1.__str__())

    L = [p1, p2, Persona("Jose", 15, 1.77)]
    print(L)


if __name__ == "__main__":
    pruebaPersona()
