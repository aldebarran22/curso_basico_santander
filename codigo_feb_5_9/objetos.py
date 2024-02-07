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
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad

    def __del__(self):
        # print('se borra a ', self.nombre)
        pass


if __name__ == "__main__":
    p1 = Persona("Pedro", 45, 1.9)
    p2 = Persona("Sara", 40, 1.88)
    # del(p1) Se fuerza la llamada al destructor de la clase: __del__

    if p2 < p1: # if p2.__lt__(p1)
        print(p2.nombre,'es menor que',p1.nombre)        
    else:
        print(p1.nombre,'es menor que',p2.nombre)

    L = [p1, p2, Persona("Ana", 42, 1.85)]
    L.sort(reverse=True)
    print(L)
    L.sort(key=lambda obj: obj.altura)
    print(L)

    print("p1 pertenece a la clase: ", p1.__class__.__name__)
    p2 = p1.__class__() # Crea un nuevo objeto
    print(p2, type(p2))


    # print(str(p1))
    # print(p1.__str__())
