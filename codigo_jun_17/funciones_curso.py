"""
Ejemplos de funciones
"""

import math

def ecuacion(a,b,c):
    raiz = b**2 - 4 * a * c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        return x1, x2
    else:
        return "No hay solución"

if __name__ == "__main__":
    solucion = ecuacion(1,5,4)
    print(solucion)
