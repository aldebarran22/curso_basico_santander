"""
Definición de parámetros dentro de una función
"""


def funcion(ob1, ob2, op1=1, op2=2, *args, **kwargs):
    print("obligatorios: ", ob1, ob2)
    print("opcionales:", op1, op2)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 10)


if __name__ == "__main__":
    funcion(10, 20)
    funcion(10, 20, 30, 40)
    funcion(10, 20, op2=40)
    funcion(1, 2, 3, 4, 5, 6, 7, 8, 9, x=100, y=200)

    print("hola", "adios", "que tal", sep=";")
