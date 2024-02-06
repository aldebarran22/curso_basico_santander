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
t = (1, 3)
print(sumar(t[0], t[1]))  # incómodo!!!
print(sumar(*t))  # Con el * desempaqueta la tupla
d = {"a": 1, "b": 3}
print(sumar(**d))  # desempaqueta el dict.

########################################################################
# Ejemplo

def formatearHora(h=0, m=0, s=0):
    print("%d:%d:%d" % (h, m, s))

horas = [(13,45,0),(8,1,34),(12,30),(17,)]
# 13:45:00, 08:01:34, 12:30:00, 17:00:00
for t in horas:
    formatearHora(*t)
