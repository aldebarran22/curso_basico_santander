"""
POO en Python. Definición de clases
"""


class Persona:
    """
    Clase persona. Propiedades y métodos
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumple(self):
        self.edad += 1

    def hablarCon(self, otro=None):
        if otro:
            print(self.nombre,'habla con ',otro.nombre)
        else:
            print(self.nombre,'habla solo')

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __del__(self):
        pass
        # print("Se está eliminando a: ", self.nombre)

if __name__ == "__main__":
    p1 = Persona("Sandra", 30, 1.7)
    p2 = Persona("Jose",44,1.76)
    print(p1.nombre)
    p1.nombre = "Eva"
    # del(p1) # Fuerza la llamada al destructor: __del__    
    print(p1)
    #print(str(p1))
    #print(p1.__str__())
    p1.cumple() # objeto.metodo()
    p2.hablarCon()
    p2.hablarCon(p1) 
