"""
Herencia simple en Python
"""


class Persona:
    """
    Implementación de la clase persona
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        # definir att.
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumple(self):
        self.edad += 1

    def hablarCon(self, otro=None):
        if otro != None:
            print(self.nombre, "habla con", otro.nombre)
        else:
            print(self.nombre, "habla solo")

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        # Vuelve a llamar al método __str__()
        return str(self)

def testPersona():
    p1 = Persona("Ana")
    p2 = Persona("Tomas")

    p2.hablarCon()
    p2.hablarCon(p1)

if __name__ == '__main__':
    testPersona()
