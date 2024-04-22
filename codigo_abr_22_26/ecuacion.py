"""
Resolver ecu. de 2 grado
ax^2 + bx + c = 0
"""
import math

# Inicialización múltiple:
#a,b,c = 1,5,4 # -1, -4
a,b,c = 1,2,3

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print(f"x1: {x1} x2: {x2}")
else:
    print('No hay solución')