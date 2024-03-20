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

    def hablar(self, other=None):
        if not other:
            print(self.nombre, "habla solo")
        else:
            print(self.nombre, "y", other.nombre, "están hablando")

    def __str__(self):
        return self.nombre + " " + str(self.peso) + " " + str(self.altura)
    
    def __repr__(self):
        return str(self)


def testPersona():
    p1 = Persona("Ana", 55, 1.8)
    p2 = Persona("Jorge", 79, 1.83)
    print(p1)
    print(p2)
    p1.hablar(p2)
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, p2, Persona("Sara", 57, 1.82)]
    print(L)
    L.sort(key=lambda obj:obj.peso)
    print(L)
    L.sort()


if __name__ == "__main__":
    testPersona()
