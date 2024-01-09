"""
Ejemplo de funciones en Python
"""


def sumar(a, b):
    return a + b


def sumar3(a, b, c):
    return a + b + c


def imprimirPosiciones(t, numero):
    ini = 0
    if numero in t:
        for i in range(t.count(numero)):
            pos = t.index(numero, ini)
            print(f"{numero} está en la posición: {pos}")
            ini = pos + 1
    else:
        print(f"{numero} no se encuentra en la tupla")


print(sumar(3, 5))
s = sumar(3, 5)
print(s)
print(sumar("55", "44"))

imprimirPosiciones((1, 5, 5, 2, 3, 4, 5), 5)
imprimirPosiciones((1, 2, 3, 4, 5), 6)
