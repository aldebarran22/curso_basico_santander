"""
Factorial recursivo
"""


def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


def testFact2():
    for i in range(1000):
        fact(900)
