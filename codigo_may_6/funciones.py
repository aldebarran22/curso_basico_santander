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

def calcularIVA(importe, iva=0.21):
    return round(importe * iva, 2)

# Forma posicional:
print(sumar("12", "34"))
print(sumar([12, 34], [1, 2, 3, 4]))
print(sumar(b=34, a=12))

print(segundos(12,30))

# Forma nominal:
print(segundos(m=30, s=15))
print(segundos(s=60))
print(segundos(12, s=60))

L = [(12,), (5,30), (8,32,45),(17,30,40)]
"""
for h,m,s in L:
    print(segundos(h,m,s))
"""

"""
for t in L:
    print(segundos(t[0], t[1], t[2]))
"""

for t in L:
    print(segundos(*t))

