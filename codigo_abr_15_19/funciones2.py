"""
Parámetros de las funciones:
Parámetros:
- obligatorios (tienen que estar a la izq en la cabecera de la función)
- opcionales
- *args --> una tupla
- **kwargs --> un diccionario
"""


def funcion(ob, op=0, *args, **kwargs):
    print("obligatorio:", ob)
    print("opcional:", op)
    print("args:", args)
    print("kwargs:", kwargs)
    print("-" * 30)

funcion()