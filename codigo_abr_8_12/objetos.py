"""
POO en Python
"""

class Persona:
    """Implementación de la clase persona"""

    def __init__(self,nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return self.nombre+" "+str(self.edad)+" "+str(self.altura)
    
    def __del__(self):
        print('eliminando: ', self.nombre)

if __name__ == '__main__':
    p1 = Persona("Ana",33, 1.8)
    print(p1)
    print(str(p1))
    print(p1.__str__())
