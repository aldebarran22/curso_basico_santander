"""
POO en Python
"""


class Persona:
    """Implementación de la clase persona"""

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    """
    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)

    """

    def hablar(self, other=None):
        if not other:
            print(self.nombre, "habla solo")
        else:
            print(self.nombre, "y", other.nombre, "están hablando")

    def __lt__(self, other):
        return self.edad < other.edad

    def __repr__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __del__(self):
        pass
        # print("eliminando: ", self.nombre)


class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0, ambito="", idiomas=[]):
        # Llamar al constructor de la clase padre:
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)
        self.ambito = ambito
        self.idiomas = idiomas

    def hablar(self, other=None):
        pass

    def __str__(self):
        # return super().__str__()+ " "+self.ambito+ " "+",".join(self.idiomas)
        return Persona.__str__(self) + " " + self.ambito + " " + ",".join(self.idiomas)


class Grupo:

    def __init__(self, nombre="", *personal):
        self.nombre = nombre
        self.grupo = []
        if len(personal) > 0:
            self.grupo.extend(personal)

    def __len__(self):
        return len(self.grupo)


def testPersona():
    p1 = Persona("Ana", 33, 1.8)
    print(p1, type(p1))
    # del(p1) Fuerza una llamada al destructor: __del__
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, Persona("Juan", 44, 1.81), Persona("Sara", 21, 1.9)]
    L.sort(key=lambda obj: obj.altura)
    print(L)
    L.sort()
    print(L)  # repr

    # Propiedades de los objetos:
    print(p1.__class__)
    print(p1.__class__.__name__)
    print(p1.__dict__)

    # Crear un objeto a través de su clase:
    p2 = p1.__class__("Lucas", 55, 1.88)
    print(p2)

    # Añadir att. en t.ejecución
    p1.__dict__["tno"] = 91258778
    p1.movil = 600909020
    print(p1.__dict__)


def testGuia():
    g1 = Guia("Sara", 44, 1.8, "I", ["Inglés", "Francés"])
    g2 = Guia("Luis", 33, 1.77, "N", ["Chino", "Italiano"])
    g1.hablar(g2)


if __name__ == "__main__":
    # testPersona()
    testGuia()
