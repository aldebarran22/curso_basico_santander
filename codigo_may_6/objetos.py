"""
POO en Python:
Diseño de clases
- Sobrecarga de operadores
- Funciones especiales 
- Listas de objetos
"""


class Persona:
    """Implementación de la clase Persona"""

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad


def pruebaPersona():
    p1 = Persona("Miguel", 34, 1.8)
    print(p1)


if __name__ == "__main__":
    pruebaPersona()
