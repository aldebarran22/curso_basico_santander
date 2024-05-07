"""
Declaración de parámetros en las funciones de Python
"""


def funcion(ob, op=0):
    print("obligatorio: ", ob)
    print("opcional: ", op)
    print("-" * 30)


if __name__ == "__main__":
    funcion(1)
    funcion(1, 2)
