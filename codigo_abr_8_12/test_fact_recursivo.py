"""
Prueba para medir el tiempo de un factorial recursivo
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def test_fact():
    for i in range(1000):
        fact(900)