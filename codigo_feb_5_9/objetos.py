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

    def __del__(self):
        # print('se borra a ', self.nombre)
        pass


if __name__ == "__main__":
    p1 = Persona("Pedro", 45, 1.9)
    p2 = Persona("Sara", 40, 1.88)
    # del(p1) Se fuerza la llamada al destructor de la clase: __del__

    L = [p1, p2, Persona('Ana',45,1.85)]
    print(L)
    for i in L:
        print(i)
    #print(str(p1))
    #print(p1.__str__())
