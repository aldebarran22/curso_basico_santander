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


class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0.0, ambito="", idiomas=[]):
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)
        self.ambito = ambito
        self.idiomas = idiomas

def testGuia():
    g1 = Guia("Laura", 24, 1.8, "I", ["inglés","francés"])
    g2 = Guia("Ana", 44, 1.7, "N", ["italiano","francés"])

    print(g1)
    if g1 < g2:
        print(g1.nombre,"es menor que",g2.nombre)
    else:
        print(g2.nombre,"es menor que",g1.nombre)

    g1.hablarCon(g2)

def testPersona():
    p1 = Persona("José", 23, 1.8)
    p2 = Persona("Paula", 22, 1.81)
    p1.hablarCon()
    p1.hablarCon(p2)


if __name__ == "__main__":
    # testPersona()
    testGuia()
