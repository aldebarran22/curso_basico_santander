"""
Ecuaciones de segundo grado
"""
import math 

# Inicialización múltiple
a,b,c = 1,5,4

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print("x1: ", x1)
    print("x2: ", x2)
else:
    print('No hay solución')
print('fin de programa')