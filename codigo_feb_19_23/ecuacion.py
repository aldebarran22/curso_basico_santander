"""
Resolver ecuaciones de segundo grado.
"""
import math
# from math import sqrt

a, b, c = 1,5,4 # a = 1, b = 5, c = 4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print('x1:', x1, 'x2:', x2)