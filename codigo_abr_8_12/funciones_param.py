"""
Tipos de parámetros en una función de Python
- obligatorios
- opcionales
- tupla: *args
- diccionario: **kwargs
"""

import matplotlib.pyplot as plt


def sumaResta(a, b):
    return a + b, a - b


def funcion(ob, op=100, *args, **kwargs):
    print("Obligatorio: ", ob)
    print("Opcional: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 20)


if __name__ == "__main__":
    # Estamos en ejecución
    funcion(1)
    funcion(1, 2, 3, 4, 5)
    d = {"x": 10, "y": 20}
    funcion(1, 2, d)
    funcion(1, 2, **d)
    funcion(d)
    funcion(1, x=100, y=200, op=999)

    # Rellenar parámetros opcionales de print
    L = list(range(10))
    for i in L:
        print(i, end=" ")
    print()

    s, r = sumaResta(1, 2)
    print(s, r)

    print("__name__", __name__)

    """
    y = [12, 44, 3, 11, 67]
    x = list(range(5))
    plt.plot(x, y, lw=3.5)
    plt.show()
    """
