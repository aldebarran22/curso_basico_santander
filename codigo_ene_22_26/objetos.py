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

    def __lt__(self, other):
        if self.edad < other.edad:
            return True
        else:
            return False

    def __del__(self):
        # print("se elimina: " + self.nombre)
        pass


if __name__ == "__main__":
    emp = Empleado(nombre="Jorge", edad=29)
    print(emp.__dict__)    
    print(emp)
    emp.cumpleaños()
    # del(emp) Llama al destructor de la clase
    print(str(emp))
    # print(emp.__str__())
    L = [emp, Empleado(1, "Gema", "Gerente", 44), Empleado(nombre="Juan", edad=34)]
    print(L)
    L.sort(key=lambda obj: obj.nombre)
    print(L)
    L.sort()
    print(L)
    L2 = [obj.__dict__ for obj in L]
    print(L2)
    emp.telefono = 600252624
    emp.__dict__['email'] = "webmaster@gmail.es"
    print(emp.__dict__)
