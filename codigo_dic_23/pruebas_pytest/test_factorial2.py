"""
Prueba del Factorial con Recursividad
"""


def fact(n):
    """
    Calcula el factorial de forma recursiva

    :param n: El factorial a calcular
    :type n: int
    :returns: int -- El factorial de n
    :raises: RecursionError
    """
    return 1 if n == 1 else n * fact(n - 1)


def test_fact():
    for i in range(1000):
        fact(1000)
