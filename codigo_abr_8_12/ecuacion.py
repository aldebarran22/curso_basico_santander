"""
Resolver ecu de 2 grado
"""
import math 

# inicializar múltiples variables:
a,b,c = 1,5,4

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print(x1, x2)
else:
    print('No hay solución')