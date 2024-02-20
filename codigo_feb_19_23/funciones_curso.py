"""
Funciones del curso de  Python
"""

L = [1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 3, 2, 1, 2]
d = dict()
for i in set(L):
    d[i] = L.count(i)