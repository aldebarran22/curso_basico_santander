"""
Implementación de funciones en Python

Formas de llamar a una función:
1) posicional: la posición que ocupan de izq a der
2) nominal: con los nombres de los parámetros
"""


def sumar(a, b):
    return a + b


def sumar3(a, b, c):
    return a + b + c

def calcularIVA(importe, iva=21):
    return round(importe * iva / 100, 2)

def segundos(h=0, m=0, s=0):
    return h*3600 + m*60 + s




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

print('IVA: ', calcularIVA(100))
print('IVA: ', calcularIVA(100, 4))
print('segundos: ', segundos(s=60))
print('segundos: ', segundos(m=5, s=30))
print('segundos: ', segundos(12,30)) # h = 12, m = 30

