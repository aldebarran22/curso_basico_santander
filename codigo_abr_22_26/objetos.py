"""
POO en Python
"""


class Empleado:
    """Implementación de la clase empleado"""

    def __init__(self, id=0, nombre="", cargo=""):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo

    def __str__(self):
        resul = ""
        for k, v in self.__dict__.items():
            resul += str(v) + " "
        return resul
        #return str(self.id) + " " + self.nombre + " " + self.cargo

    def __del__(self):
        pass
        # print('Eliminando a ', self.nombre)


def testEmpleado():
    emp = Empleado(12, "Pedro", "Ventas")
    print(emp)
    print(str(emp))
    print(emp.__str__())


if __name__ == "__main__":
    testEmpleado()
