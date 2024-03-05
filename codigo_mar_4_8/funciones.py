"""
Funciones en Python
- Llamar a una función
"""


def sumar(a, b):
    """Suma los dos parámetros que recibe"""
    return a + b


# Formas de llamar a la función
# 1) forma posicional:
print(sumar(12, 34))

# 2) forma nominal:
print(sumar(b=34, a=12))
