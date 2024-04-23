"""
Pasar por parámetro una función y ejecutarla
"""


def sumar(a, b):
    return a + b

def mulCadena(cad, n=10):
    return cad * n

def ejecutar(f, *args, **kwargs):
    return f(*args, **kwargs)

if __name__ == '__main__':
    print(ejecutar(sumar, 12,34))
    print(ejecutar(mulCadena, "hola"))