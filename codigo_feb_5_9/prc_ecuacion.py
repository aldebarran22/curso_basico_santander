"""
Resolver una ecuación de 2º grado en Python
ax^2 + bx + c = 0
"""
import math

a = 1
b = 5
c = 4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print(x1, x2)