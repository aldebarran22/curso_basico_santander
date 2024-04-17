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

    def __del__(self):
        print("Eliminando a: ", self.nombre)


if __name__ == "__main__":
    p1 = Persona("Ana")
    p2 = Persona("Pedro", 33)
    p3 = Persona("Juan", altura=1.8)

    print(p1) # str(p1) p1.__str__()
    print(str(p1))
    print(p1.__str__())
