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


print(calcularIVA(100))
print(calcularIVA(100, 4))
