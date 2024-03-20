"""
P.O.O en Python
"""


class Persona:
    """Implementación de la clase persona"""

    criterio = "nombre"

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

    def getCabeceras(self):
        return ";".join([v for v in self.__dict__.keys()])

    """
    def __str__(self):
        return ";".join([str(v) for v in self.__dict__.values()])
    """

    def __repr__(self):
        return str(self)

    """
    def __lt__(self, other):
        return self.nombre < other.nombre
    """

    def __lt__(self, other):
        campo1 = self.__dict__[Persona.criterio]
        campo2 = other.__dict__[Persona.criterio]
        return campo1 < campo2


class Empleado(Persona):

    def __init__(self, nombre="", peso=0, altura=0, empresa="", sueldo=0.0, idiomas=[]):
        # super().__init__(nombre, peso, altura)
        Persona.__init__(self, nombre, peso, altura)
        self.empresa = empresa
        self.sueldo = sueldo
        self.idiomas = idiomas

    def __str__(self):
        return Persona.__str__(self) + " " + self.empresa + " " + str(self.sueldo)+" "+",".join(self.idiomas)


def testPersona():
    p1 = Persona("Tomás", 69, 1.8)
    p2 = Persona("Jorge", 70, 1.83)
    print(p1)
    print(p2)
    p1.hablar(p2)
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, p2, Persona("Sara", 70, 1.82)]
    print(L)
    L.sort(key=lambda obj: (obj.peso, obj.nombre))
    print(L)
    L.sort()
    print(L)
    Persona.criterio = "altura"
    L.sort(reverse=True)
    print(L)
    """
    p1.telefono = 912550099
    p1.__dict__['movil'] = 600898979
    """
    print(p1)

    txt = p1.getCabeceras() + "\n" + "\n".join(str(obj) for obj in L)
    print(txt)


def testEmpleado():
    emp1 = Empleado("Pedro", 77, 1.8, "Santander", 2000.0, ['inglés','alemán'])
    print(emp1)


if __name__ == "__main__":
    # testPersona()
    testEmpleado()
