"""
POO en Python
"""


class Persona:
    """
    Implementación de la clase persona
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        # definición de atributos
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)  # Red. a __str__

    def __lt__(self, other):
        return self.edad < other.edad

    def __eq__(self, other):
        return (
            self.nombre == other.nombre
            and self.edad == other.edad
            and self.altura == other.altura
        )

    def __del__(self):
        # print("se borra a: ", self.nombre)
        pass


def testPersona():
    p2 = Persona("Juan")
    p3 = Persona("Juan")
    # del p2  # Fuerza la llamada al destructor --> __del__()
    p1 = Persona("Andrés", 34, 1.8)
    print(p1)  # str(p1) --> p1.__str__()
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, Persona("Ana", 45, 1.77), Persona("Jose", 66, 1.9)]
    print(L)
    L.sort(key=lambda obj: obj.altura)
    print(L)
    L.sort()  # Utiliza __lt__()
    print(L)
    if L[0] < L[1]:  # if L[0].__lt__(L[1]):
        print(L[0], "es menor que", L[1])
    else:
        print(L[1], "es menor que", L[0])

    p4 = p2
    print("p2 == p3", p2 == p3)
    print("p2 == p4", p2 == p4)  # por defecto comprueba las refs. no los att.
    print("id(p2)", id(p2))
    print("id(p4)", id(p4))


def testCrearObjetos():
    pass


if __name__ == "__main__":
    # testPersona()
    testCrearObjetos()
