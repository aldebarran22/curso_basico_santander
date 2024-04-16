"""
Implementación de funciones en Python

Formas de llamar a una función:
1) posicional: la posición que ocupan de izq a der
2) nominal: con los nombres de los parámetros
"""


def sumar(a, b):
    return a + b


def sumar3(a, b, c):
    """Sumar 3 variables"""
    return a + b + c


def calcularIVA(importe, iva=21):
    return round(importe * iva / 100, 2)


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


# Con tipos anotados: funcionan a título informativo.
def concatenar(a: str, b: str) -> str:
    return a + b


print("Resul: ", sumar(12, 34))
print("Resul: ", sumar("12", "34"))
print("Resul: ", sumar(12.4, 34.7))
print("Resul: ", sumar([12, 12], [34, 34]))
print("Concatenar: ", concatenar(34, 77))

# Nominal:
print("Resul: ", sumar(b=34, a=12))

print("IVA: ", calcularIVA(100))
print("IVA: ", calcularIVA(100, 4))
print("segundos: ", segundos(s=60))
print("segundos: ", segundos(m=5, s=30))
print("segundos: ", segundos(12, 30))  # h = 12, m = 30

print("-" * 30)
print("Con tuplas:")
t = (12, 45, 34)
print("Segundos: ", segundos(t[0], t[1], t[2]))
print("Segundos: ", segundos(*t))

print("-" * 30)
print("Con diccionarios:")
d = {"h": 12, "m": 45, "s": 34}
print("Segundos: ", segundos(d["h"], d["m"], d["s"]))
print("Segundos: ", segundos(**d))

print("-" * 30)
print("Con Listas:")
t = [12, 45, 34]
print("Segundos: ", segundos(*t))
