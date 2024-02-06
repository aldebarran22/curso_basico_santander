"""
Formas de llamar a una función en Python
1) Posicional
2) Nominal
3) Con una tupla / lista
4) Con un diccionario
"""


def sumar(a, b):
    return a + b


print(sumar(1, 3))  # Posicional
print(sumar(b=3, a=1))  # Nominal
t = (1,3)
print(sumar(t[0], t[1])) # incómodo!!!
print(sumar(*t)) # Con el * desempaqueta la tupla
