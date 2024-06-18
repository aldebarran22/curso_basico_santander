"""
Tipos de parámetros de una función:
- obligatorios
- opcionales
- una tupla: *args
- un diccionarios: **kwargs

Tipos anotados
"""

def sumar(a:str, b:str) -> str:
    return a + " " + b

print(sumar("hola","adios"))
print(sumar(12,34))