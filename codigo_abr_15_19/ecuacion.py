"""
Calcular ecuaciones de 2 grado en Python
ax^2 + bx + c = 0
"""

import math

# Inicialización múltiples:
a,b,c = 1,5,4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print("x1:",x1,"x2:",x2)

#f-string
print(f"x1: {x1}, x2: {x2}")

