"""
Ecuaciones de segundo grado
"""
import math 

# Inicialización múltiple
a,b,c = 1,5,4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print("x1: ", x1)
print("x2: ", x2)