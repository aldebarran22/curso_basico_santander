"""
POO en Python. Definición de clases
"""


class Persona:
    """
    Clase persona. Propiedades y métodos
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __del__(self):
        pass
        # print("Se está eliminando a: ", self.nombre)


if __name__ == "__main__":
    p1 = Persona("Sandra", 30, 1.7)
    print(p1.nombre)
    p1.nombre = "Eva"
    # del(p1) # Fuerza la llamada al destructor: __del__
    print("continua el programa")
    print(p1)
    print(str(p1))
    print(p1.__str__())
