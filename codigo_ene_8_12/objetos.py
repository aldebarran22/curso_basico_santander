"""
Diseño orientado a objetos en Python
Implementar clases y utilización
Colecciones de objetos
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

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        # Vuelve a llamar al método __str__()
        return str(self)


if __name__ == "__main__":
    p1 = Persona("Pedro", 33, 1.8)
    p2 = Persona("Juan", 30, 1.82)
    if p1 < p2:  # if p1.__lt__(p2)
        print(p1, "menor que", p2)
    else:
        print(p2, "menor que", p1)
    print(p1)
    p1.cumple()
    print(p1)
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, Persona("Ana", 45, 1.77), Persona("Sara", 23, 1.88)]
    print(L)
    L.sort(key=lambda obj: obj.altura, reverse=True)
    L.sort()
    print(L)
