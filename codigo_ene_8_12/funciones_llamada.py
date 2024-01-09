"""
Distintas formas de llamar a una función en Python
4 formas:
1) posicional: por la posición que ocupa el parámetro
2) nominal: está relacionada con el nombre de los parámetros
"""


def f1(h=0, m=0, s=0):
    print(h, m, s)


def sumar(a, b):
    return a + b


if __name__ == "__main__":
    # Posicional
    print(sumar(1, 2))
    f1(0, 0, 30)

    # nominal
    print(sumar(b=2, a=1))
    f1(s=30)
