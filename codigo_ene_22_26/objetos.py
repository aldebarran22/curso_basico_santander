"""
Ejemplos de programación orientada a objetos en Python
Definir una clase y las operaciones típicas.
"""


class Empleado:
    """
    Propiedades y operadores de la clase Empleado
    """

    def __init__(self, id=0, nombre="", cargo="", edad=0):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.edad = edad

    def __str__(self):
        return (
            str(self.id) + " " + self.nombre + " " + self.cargo + " " + str(self.edad)
        )


if __name__ == "__main__":
    emp = Empleado(nombre="Jorge", edad=29)
    print(emp)
