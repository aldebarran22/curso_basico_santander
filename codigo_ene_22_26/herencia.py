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


class Extranjero(Persona):
    def __init__(self, nombre="", edad=0, altura=0.0, idiomas=[]):
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)
        self.idiomas = idiomas

    def hablarCon(self, otro=None):
        if otro == None:
            Persona.hablarCon(self, otro)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)

            comunes = c1 & c2
            if len(comunes) > 0:
                print(
                    self.nombre
                    + " habla con "
                    + otro.nombre
                    + " en "
                    + " o ".join(comunes)
                )
            else:
                print("No tienen un idioma en común")

    def __str__(self):
        return super().__str__() + " " + ",".join(self.idiomas)


def testPersona():
    p1 = Persona("Ana")
    p2 = Persona("Tomas")

    p2.hablarCon()
    p2.hablarCon(p1)


def testExtranjero():
    ex1 = Extranjero("Pedro", 24, 1.77, ["inglés", "francés"])
    ex2 = Extranjero("Sara", 22, 1.67, ["inglés", "francés", "alemán"])
    print(ex1)
    ex1.cumple()
    print(ex1)
    ex1.hablarCon(ex2)


if __name__ == "__main__":
    # testPersona()
    testExtranjero()
