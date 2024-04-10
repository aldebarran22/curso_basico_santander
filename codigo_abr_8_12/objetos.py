"""
POO en Python
"""

class Persona:
    """Implementación de la clase persona"""

    def __init__(self,nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

if __name__ == '__main__':
    p1 = Persona("Ana",33, 1.8)
    print(p1)
