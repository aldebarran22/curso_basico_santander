"""
POO en Python
"""


class Persona:
    """Implementación de la clase persona"""

    contador = 0

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

        Persona.contador += 1

    @staticmethod
    def getContador():
        return Persona.contador

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
        Persona.contador -= 1
        # print("eliminando: ", self.nombre)


class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0, ambito="", idiomas=[]):
        # Llamar al constructor de la clase padre:
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)
        self.ambito = ambito
        self.idiomas = idiomas

    def hablar(self, other=None):
        if not other:
            Persona.hablar(self, other)
        else:
            c1 = set(self.idiomas)
            c2 = set(other.idiomas)
            comun = c1 & c2
            if len(comun) == 0:
                raise Exception("No pueden hablar")
            else:
                print(
                    self.nombre,
                    "y",
                    other.nombre,
                    "pueden hablar en: ",
                    " o ".join(comun),
                )

    def __str__(self):
        # return super().__str__()+ " "+self.ambito+ " "+",".join(self.idiomas)
        return Persona.__str__(self) + " " + self.ambito + " " + ",".join(self.idiomas)


class Grupo:

    def __init__(self, nombre="", *personal):
        self.nombre = nombre
        self.grupo = []
        self.indice = -1
        if len(personal) > 0:
            self.grupo.extend(personal)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice + 1 == len(self.grupo):
            self.indice = -1  # Para volver a repetir
            raise StopIteration
        self.indice = self.indice + 1
        return self.grupo[self.indice]

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
    g1 = Guia("Sara", 44, 1.8, "I", ["Inglés", "Francés", "Chino"])
    g2 = Guia("Luis", 33, 1.77, "N", ["Chino", "Italiano", "Inglés"])
    g1.hablar(g2)


def testGrupo():
    print("Num personas:", Persona.getContador())
    p1 = Persona("Ana", 33, 1.8)
    g1 = Guia("Pedro", 44, 1.8, "I", ["Inglés", "Francés", "Chino"])
    p2 = Persona("Juan", 44, 1.81)
    p3 = Persona("Sara", 21, 1.9)
    print("Num personas:", Persona.getContador())
    grupo = Grupo("Viaje Noruega", p1, p2, p3, g1)
    print("número de personas del grupo: ", len(grupo))
    for i in grupo:
        print(i)

def testAtributos():
    p1 = Persona("Ana", 33, 1.8)
    if hasattr(p1, "edad"):
        print(getattr(p1, "edad"))

    cad = "{}({},{},{})".format("Persona","'Ana'",33,1.8)
    print(cad)
    obj = eval(cad)
    print(obj)
    print(obj.__class__.__name__)


if __name__ == "__main__":
    # testPersona()
    # testGuia()
    # testGrupo()
    testAtributos()
