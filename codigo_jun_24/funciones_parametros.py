"""
Parámetros que puede recibir una función:
- obligatorios
- opcionales
- una tupla: *args
- un diccionario: **kwargs
"""


def funcion(ob, op=1, *args, **kwargs):
    print("obligatorio: ", ob)
    print("opcionales: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print()


if __name__ == "__main__":
    funcion(100)
