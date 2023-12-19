"""
Tipos de parámetros en una función de Python
"""


def funcion(ob1, ob2, op1=1, op2=2, *args, s="", **kwargs):
    print("obligatorios: ", ob1, ob2)
    print("opcionales: ", op1, op2)
    print("args: ", args)
    print("s: ", s)
    print("kwargs: ", kwargs)
    print()


if __name__ == "__main__":
    funcion(10, 20)
    funcion(10, 20, op2=200)
    funcion(1, 2, 3, 4)
    funcion(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, s="hola", x=10, y=20)
