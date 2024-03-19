"""
Tipos de parámetros en las funciones de python:
- obligatorios
- opcionales
- número indeterminado (tupla)
- número indeterminado con claves (diccionario)
Tipos anotados
"""


# Uno obligatorio y otro opcional:
def calcularIVA(importe, iva=21):
    return round(importe * iva / 100, 2)


# Tipos anotados:
def sumar(a:str, b:str) -> str:
    return a + b

print(calcularIVA(100))
print(calcularIVA(100, 4))
print(sumar("hola", "adios"))
print(sumar(12,34))

