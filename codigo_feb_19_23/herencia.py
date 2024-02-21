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

    def hablarCon(self, other=None):
        if other is None:
            Persona.hablarCon(self)
        else:
            c1 = set(self.idiomas)
            c2 = set(other.idiomas)
            comun = c1 & c2
            if len(comun) == 0:
                raise ValueError("No pueden hablar")
            else:
                print("Puede hablar en: ", " o ".join(comun))

    def __str__(self):
        return Persona.__str__(self) + " " + self.ambito + " " + ",".join(self.idiomas)
        # return super().__str__() + " " + self.ambito + " " + ",".join(self.idiomas)


def testGuia():
    g1 = Guia("Andrés", 34, 1.8, "I", ["Inglés", "Francés", "Alemán"])
    g1.cumple()
    print(g1)
    g2 = Guia("Eva", 34, 1.8, "I", ["Alemán", "Chino", "Inglés"])
    g1.hablarCon(g2)


if __name__ == "__main__":
    testGuia()
