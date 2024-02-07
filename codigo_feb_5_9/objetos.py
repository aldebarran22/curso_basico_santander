"""
POO en Python
"""

class Persona:
    """
    Implementar la clase Persona
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definición de atributos:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return self.nombre+" "+str(self.edad)+" "+str(self.altura)


if __name__ == "__main__":
    p1 = Persona('Pedro',45, 1.9)
    print(p1)
    print(str(p1))
    print(p1.__str__())
