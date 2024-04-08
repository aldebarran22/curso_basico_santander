"""
Resolver ecu de 2 grado
"""
import math 

# inicializar múltiples variables:
a,b,c = 1,5,4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print(x1, x2)