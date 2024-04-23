"""
Funciones en python:
Paso de parámetros y tipos de parámetros:
- obligatorios
- opcionales
- tupla
- diccionario

- Tipos anotados
"""


def saludar(nombre):
    return "Hola " + nombre.capitalize()


def saludar2(nombre: str) -> str:
    return "Hola " + nombre.capitalize()


def sumar(a: int, b: int) -> int:
    return a + b


print(sumar(23, 45))
print(sumar("23", "45"))
print(sumar([23], [45]))


print()
