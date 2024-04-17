"""POO en Python."""


class Persona:
    """Implementación de la clase persona"""

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definir att de la clase:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        if self.edad < other.edad:
            return True
        else:
            return False

    def __del__(self):
        pass
        # print("Eliminando a: ", self.nombre)


if __name__ == "__main__":
    p1 = Persona("Ana", 47, 1.76)
    p2 = Persona("Pedro", 33, 1.8)
    p3 = Persona("Juan", 45, altura=1.82)

    L = [p1, p2, p3, Persona("Sonia", 23, 1.77)]
    print(L)
    # Ordenar por Edad ASC
    L.sort(key=lambda obj: obj.edad)
    print(L)
    # Ordenar por altura DESC
    L.sort(key=lambda obj: obj.altura, reverse=True)
    print(L)

    L.sort()
    print("L.sort() -> ",L)

    # print(str(p1))
    # print(p1.__str__())
