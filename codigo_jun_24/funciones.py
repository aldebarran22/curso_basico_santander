"""
Definición de funciones en Python.
Tipos de llamada:
- posicional
- nominal
- con una tupla (vale también lista)
- con un diccionario
"""


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


def calcularIVA(precio, iva=0.21):
    return round(precio * iva, 2)


def sumar(a: str, b: str) -> str:
    """Retorna la suma de los dos parámetros"""
    return a + b


def restar(a, b):
    """Retorna la resta de los dos parámetros"""
    return a - b


def restar3(a, b, c):
    return a - b - c


if __name__ == "__main__":
    print("__name__ ", __name__)
    print("suma:", sumar(12, 88))
    print("restar: ", restar(12, 4))
    print("iva: ", calcularIVA(200, 0.04))

    print("30 min: ", segundos(m=30))
    print("05:30 ", segundos(5, 30))
