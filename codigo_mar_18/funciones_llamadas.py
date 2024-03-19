"""
Funciones en Python:
Formas de llamar a una función en Python
1- Posicional
2- Nominal
3- Tupla / lista
4- diccionario
Tipos anotados
"""


def sumar(a, b):
    return a + b


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


# posicional:
print(sumar(1, 2))
print(segundos(12, 30))  # 12:30:00

# nominal:
print(sumar(b=2, a=1))
print(segundos(m=10, s=15))  # 00:10:15
print(segundos(12, s=10))  # 12:00:10

# Con tuplas / listas:
L = [[12, 30, 10], (8, 25, 12), (17, 8, 19)]
for t in L:
    print(t, segundos(t[0], t[1], t[2]))
    print(t, segundos(*t))

for h, m, s in L:
    print(segundos(h, m, s))

# Con un diccionario:
d = {"h": 12, "m": 30, "s": 15}
print(d, segundos(**d))
