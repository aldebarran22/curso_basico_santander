"""
Declaración de parámetros en las funciones de Python
"""


def funcion(ob, op=0, *args):
    print("obligatorio: ", ob)
    print("opcional: ", op)
    print('args: ', args)
    print("-" * 30)


if __name__ == "__main__":
    funcion(1)
    funcion(1, 2)
    funcion(1,2,3,4,5,6)
