"""
Prueba para un factorial iterativo
"""

def fact(n):
    resul = 1
    for i in range(1,n+1):
        resul *= i
    return resul

def test_fact2():
    for i in range(1000):
        fact(900)