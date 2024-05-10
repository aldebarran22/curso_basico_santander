"""
Factorial iterativo
"""


def fact(n):
    resul = 1
    for i in range(1, n + 1):
        resul *= i
    return resul


def testFact1():
    for i in range(1000):
        fact(900)
