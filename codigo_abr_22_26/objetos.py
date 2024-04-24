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

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.id < other.id

    def __del__(self):
        pass
        # print('Eliminando a ', self.nombre)


def testEmpleado():
    emp = Empleado(12, "Pedro", "Ventas")
    emp2 = Empleado(15, "Alberto", "Contabilidad")
    print(emp)
    L = [emp, emp2, Empleado(23, "Ana", "Gerente")]
    print(L)
    L.sort(reverse=True)    
    print(L)
    L.sort(key=lambda obj: obj.nombre)
    print(L)
    exit()
    #print(str(emp))
    #print(emp.__str__())
    emp.tno = 915887788
    emp.__dict__['movil'] = 600998877
    print(emp)

    if emp < emp2: # if emp.__lt__(emp2):
        print("emp < emp2")
    else:
        print("emp2 < emp")


if __name__ == "__main__":
    testEmpleado()
