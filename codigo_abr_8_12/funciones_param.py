"""
Tipos de parámetros en una función de Python
- obligatorios
- opcionales
- tupla: *args
- diccionario: **kwargs
"""


def funcion(ob, op=100, *args, **kwargs):
    print("Obligatorio: ", ob)
    print("Opcional: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 20)

funcion(1)
funcion(1,2,3,4,5)
