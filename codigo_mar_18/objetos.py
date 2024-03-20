"""
P.O.O en Python
"""


class Persona:
    """Implementación de la clase persona"""

    def __init__(self, nombre="", peso=0, altura=0.0):
        # Definición de att.
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return self.nombre + " " + str(self.peso) + " " + str(self.altura)


def testPersona():
    p1 = Persona("Ana", 55, 1.8)
    print(p1)


if __name__ == "__main__":
    testPersona()
