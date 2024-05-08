"""
POO: en Python
Herencia múltiple
No hay inteface, pero si clases Abstractas: heredar abc.ABC
sobrecarga de operadores
str()  ->> __str__()
len()  --> __len__

<, <=, >=, >, ==, !=  -> __lt__, __le__, __ge__, __gt__

+, -,  -> __add__, __sub__

"""


class Persona:

    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad


    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return self.nombre + " " + str(self.edad)


p = Persona("Jose", 45)

p2 = Persona("Gema", 44)
print(p.__dict__)
p.__dict__["tno"] = 9122236665
p.movil = 600678899
print(p.__dict__)
print(p.tno)

if p < p2: # p.__lt__(p2)
    print('el menor es: ', p)
else:
    print('el menor es: ', p2)