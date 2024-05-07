"""
Declaración de parámetros en las funciones de Python
"""

import matplotlib.pyplot as plt


def generarGrafica():
    x = list(range(5))
    y = [12, 5, 6, 23, 7]
    plt.plot(x, y, color="red", linewidth=5)
    plt.show()


def funcion(ob, op=0, *args, **kwargs):
    print("obligatorio: ", ob)
    print("opcional: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 30)


if __name__ == "__main__":
    generarGrafica()
    exit()

    funcion(1)
    funcion(1, 2)
    funcion(1, 2, 3, 4, 5, 6)
    funcion(1, 2, 3, 4, 5, 6, x=10, y=20)

    # print("hola", "adios", sep="_")
