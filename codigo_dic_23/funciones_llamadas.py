"""
Formas de llamar a una función en Python
1. forma posicional
2. forma nominal
3. tupla / lista
4. diccionario
"""


def sumar(a, b):
    """Suma los valores a y b"""
    return a + b


if __name__ == "__main__":
    print("posicional: ", sumar(1, 2))
    print("nominal: ", sumar(b=2, a=1))
    t = (1, 2)
    print("con una tupla: ", sumar(*t))  # sumar(t[0], t[1])
    d = {"a": 1, "b": 2}
    print("con un diccionario:", sumar(**d))
    L = [1, 2]
    print("con una lista: ", sumar(*L))
