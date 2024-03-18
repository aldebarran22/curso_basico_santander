"""ecuacion.py

Resolver la ecu de 2 grado
"""

import math

a,b,c = 1,5,4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

# f-string
print(f"x1 = {x1}")
print(f"x2 = {x2}")
