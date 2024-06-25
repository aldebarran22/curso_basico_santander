"""
Definición de funciones en Python.
Tipos de llamada:
- posicional
- nominal
- con una tupla (vale también lista)
- con un diccionario
"""


def sumar(a: str, b: str) -> str:
    """Retorna la suma de los dos parámetros"""
    return a + b


def restar(a, b):
    """Retorna la resta de los dos parámetros"""
    return a - b


if __name__ == "__main__":
    print("__name__ ", __name__)
    print("suma:", sumar(12, 88))
