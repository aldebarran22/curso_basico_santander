"""
Implementación de funciones en Python
"""


def sumar(a, b):
    return a + b


def concatenar(a: str, b: str) -> str:
    return a + b


print("Resul: ", sumar(12, 34))
print("Resul: ", sumar("12", "34"))
print("Resul: ", sumar(12.4, 34.7))
print("Resul: ", sumar([12, 12], [34, 34]))
print('Concatenar: ', concatenar(34,77))