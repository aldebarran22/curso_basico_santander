"""
Ejemplo de herencia simple
"""


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

    def __lt__(self, other):
        return self.edad < other.edad

    def hablarCon(self, other=None):
        if other is None:
            print(self.nombre, "habla solo")
        else:
            print(self.nombre, "y", other.nombre, "están hablando")


class Guia:
    pass


def testPersona():
    p1 = Persona("José", 23, 1.8)
    p2 = Persona("Paula", 22, 1.81)
    p1.hablarCon()
    p1.hablarCon(p2)


def testGuia():
    pass


if __name__ == "__main__":
    # testPersona()
    testGuia()
