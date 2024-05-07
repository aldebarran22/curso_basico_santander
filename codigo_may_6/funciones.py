"""
Funciones en Python.
- Tipos anotados
- Formas de llamar a una función:
-1) forma posicional
-2) forma nominal (el nombre de los parámetros)
"""


def sumar3(a: str, b: str, c: str) -> str:
    return a + b + c


# Tipos anotados:
def sumar(a: int, b: int) -> int:
    return a + b


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s

# Forma posicional:
print(sumar("12", "34"))
print(sumar([12, 34], [1, 2, 3, 4]))
print(sumar(b=34, a=12))

print(segundos(12,30))

# Forma nominal:
print(segundos(m=30, s=15))
