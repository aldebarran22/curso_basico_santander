"""
Funciones en Python:
Llamar a una función:
- 1) Forma posicional
- 2) Forma nominal
- 3) A partir de una tupla / lista
- 4) A partir de un diccionario

Tipos anotados.
"""


def limpiarCad(cad: list) -> str:
    pass


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


def sumar(a: int, b: int) -> int:
    return a + b


def sumar3(a, b, c):
    return a + b + c


def ejemplo():
    """Documentación de la función ejemplo"""
    pass


print(sumar((1,), (2,)))


ejemplo()

# 1) posicional
print(sumar(1, 2))
# 2) nominal
print(sumar(b=2, a=1))
print(segundos(m=40))
# 12:00:10
print(segundos(12, s=10))
# 00:30:45
# print(segundos(m=30, 45)) Error, no podemos utilizar forma posicional
# despues de un parámetro nominal
print(segundos(m=30, s=45))

# 3) Con una tupla
t = (1, 2)
print(sumar(*t))

L = [1, 2]
print(sumar(*L))

# 4) Con un diccionario:
d = {"a": 1, "b": 2}
print(sumar(**d))

# Convertir las horas de la lista L en segundos y almacenar
# el resultado en otra lista:
L = [(12, 3, 45), (7, 0, 1), (11, 6, 7), (9, 56, 7)]
R = list()
for t in L:
    R.append(segundos(*t))

R2 = []
for h, m, s in L:
    R2.append(segundos(h, m, s))

print(R)
print(R2)
