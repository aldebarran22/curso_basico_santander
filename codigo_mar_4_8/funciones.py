"""
Funciones en Python
- Llamar a una función
"""


def sumar(a, b):
    """Suma los dos parámetros que recibe"""
    return a + b


def calcularIVA(importe, tasa=2, iva=21):
    return round((importe + tasa) * iva / 100, 2)


# Formas de llamar a la función
# 1) forma posicional:
print(sumar(12, 34))
print(calcularIVA(100, 5, 10))

# 2) forma nominal:
print(sumar(b=34, a=12))
print(calcularIVA(100, iva=21))
