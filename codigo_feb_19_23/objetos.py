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

    def __del__(self):
        # print("se borra a: ", self.nombre)
        pass


if __name__ == "__main__":
    p2 = Persona("Juan")
    del p2  # Fuerza la llamada al destructor --> __del__()
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
