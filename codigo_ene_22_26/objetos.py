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
    
    def __repr__(self):
        return str(self)

    def cumpleaños(self):
        self.edad += 1

    def __del__(self):
        # print("se elimina: " + self.nombre)
        pass


if __name__ == "__main__":
    emp = Empleado(nombre="Jorge", edad=29)
    print(emp)
    emp.cumpleaños()
    # del(emp) Llama al destructor de la clase
    print(str(emp))
    # print(emp.__str__())
    L = [emp, Empleado(1, "Gema", "Gerente", 44), Empleado(nombre="Juan", edad=34)]
    print(L)