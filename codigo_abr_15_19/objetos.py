"""POO en Python."""


class Persona:
    """Implementación de la clase persona"""

    # Att de clase:
    numPersonas = 0

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definir att de la clase:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

        Persona.numPersonas+=1
    """
    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)
    """

    @staticmethod
    def getNumPersonas():
        return Persona.numPersonas

    def __str__(self):
        resul = ""
        for k, v in self.__dict__.items():
            resul += k + " = " + str(v) + "\n"

        return resul

    def __repr__(self):
        return str(self)  # return self.__str__()

    def __lt__(self, other):
        if self.edad < other.edad:
            return True
        else:
            return False

    def __eq__(self, other):
        return (
            self.nombre == other.nombre
            and self.edad == other.edad
            and self.altura == other.altura
        )

    def __del__(self):
        Persona.numPersonas-=1
        # print("Eliminando a: ", self.nombre)

class Grupo:
    pass


if __name__ == "__main__":
    print('NumPersonas. ', Persona.getNumPersonas())
    p1 = Persona("Ana", 47, 1.76)
    p2 = Persona("Pedro", 46, 1.75)
    p3 = Persona("Juan", 45, altura=1.82)
    person1 = Persona('Angel')
    print('NumPersonas. ', Persona.getNumPersonas())
    del person1
    print('NumPersonas. ', Persona.getNumPersonas())

    if p1 == p2:
        print("p1 y p2 son iguales")
    else:
        print("Son distintos")

    L = [p1, p2, p3, Persona("Sonia", 23, 1.77)]
    print(L)
    # Ordenar por Edad ASC
    L.sort(key=lambda obj: obj.edad)
    print(L)
    # Ordenar por altura DESC
    L.sort(key=lambda obj: obj.altura, reverse=True)
    print(L)

    L.sort()
    print("L.sort() -> ", L)

    # print(str(p1))
    # print(p1.__str__())

    print(p1.__dict__)
    p1.__dict__["tno"] = 912233445
    p1.movil = 600455654
    print(p1.__dict__)
    del p1.nombre  # Borra el att
    print(p1) 
    print(p1.__class__)
    print(p1.__class__.__name__)

    # Crear objetos:
    persona1 = p1.__class__("Jorge")
    print(persona1)
