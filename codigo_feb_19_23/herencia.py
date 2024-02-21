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

    def __str__(self):
        return Persona.__str__(self) + " "+self.ambito+" "+",".join(self.idiomas)

def testGuia():
    g1 = Guia("Andrés", 34, 1.8, 'I', ['Inglés','Francés'])
    g1.cumple()
    print(g1)


if __name__ == "__main__":
    testGuia()
