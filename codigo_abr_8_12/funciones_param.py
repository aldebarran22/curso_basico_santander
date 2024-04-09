"""
Tipos de parámetros en una función de Python
- obligatorios
- opcionales
- tupla: *args
- diccionario: **kwargs
"""


def funcion(ob, op=100, *args, **kwargs):
    print("Obligatio: ", ob)
    print("opcional: ", op)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print("-" * 20)
