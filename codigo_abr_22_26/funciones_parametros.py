"""
Paso de parámetros y tipos de parámetros:
- obligatorios
- opcionales
- tupla
- diccionario

Formas de llamar a una función (con respecto a los parámetros):
- Posicional
- Nominal
- Con una tupla (con una lista)
- Con un diccionario
"""


def sumar(a, b):
    return a + b


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


def calcularIVA(importe, iva=21):
    return round(importe * iva / 100, 2)


# 1) Forma posicional
print(sumar(3, 4))

# 2) Nominal:
print(sumar(b=4, a=3))
print(segundos(12, 30))
print(segundos(m=5))
print(segundos(m=5, s=30))
print(segundos(12, s=30))

print(calcularIVA(100))
print(calcularIVA(100, 4))
