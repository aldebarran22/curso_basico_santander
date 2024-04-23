"""
Paso de parámetros y tipos de parámetros:
- obligatorios
- opcionales
- tupla
- diccionario

Formas de llamar a una función (con respecto a los parámetros):
- Posicional
- Nominal
- Con una tupla (con una lista)
- Con un diccionario
"""

import matplotlib.pyplot as plt

x = list(range(5))
y = [10, 40, 23, 55, 2]
plt.plot(x, y, color="green", lw=5)
plt.show()


def sumar(a, b):
    return a + b


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


def calcularIVA(importe, iva=21):
    return round(importe * iva / 100, 2)


def funcion(ob, op=0, *args, **kwargs):
    print("obligatorio: ", ob)
    print("opcional: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 20)


if __name__ == "__main__":
    funcion(1)
    funcion(1, 2, 3, 4, 5, 6, 7, 8, x=100, y=200)

    # 1) Forma posicional
    print(sumar(3, 4))

    # 2) Nominal:
    print(sumar(b=4, a=3))
    print(segundos(12, 30))
    print(segundos(m=5))
    print(segundos(m=5, s=30))
    print(segundos(12, s=30))

    print(calcularIVA(100))
    print(calcularIVA(100, 4))

    # Con una tupla:
    t = (3, 4)
    print(sumar(*t))

    L = [3, 4]
    print(sumar(*L))

    d = {"a": 3, "b": 4}
    print(sumar(**d))

    # Convertir la lista de horas en segundos:
    SG = []
    L = [(12,), (11, 40), (8, 32, 15), (9, 45, 11)]
