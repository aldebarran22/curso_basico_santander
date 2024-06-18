"""
Funciones en Python
"""


def sumar(a, b):
    """
    Suma los dos parámetros que recibe
    """
    return a + b


def sumar3(a, b, c):
    return a + b + c


def segundos(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


if __name__ == "__main__":
    # Formas de llamar a una función en Python:
    # posicional:
    print(segundos(13, 46, 18))  # 13:46:18

    # nominal:
    # 12:00:04
    print(segundos(12, s=4))
    # 00:56:03
    print(segundos(m=56, s=3))
    print(s=9, h=23, m=8) # 23:08:09

    # Con una tupla (vale también una lista)
    t = (12,34,6)
    #print(segundos(t[0], t[1], t[2]))
    print(segundos(*t))
