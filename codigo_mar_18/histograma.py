"""
Obtener un histograma con los valores que
se repiten en una lista.
"""

import random

# range(ini, fin-1, salto=1)
print(list(range(10)))
print(list(range(1,11)))
print(list(range(0,101, 5)))
print(list(range(-10, 1, 1)))
print(list(range(-10, -30, -2)))

# Cargar una lista de números aleatorios:
L = []
for i in range(1000):
    L.append(random.randint(1,20))
print(L[:10])
claves = set(L)
histo = dict()
print(claves)
for k in claves:
    #print(k, L.count(k))
    histo[k] = L.count(k)

L = sorted(histo.items(), key=lambda t: t[1], reverse=True)
print(L)
print(type(histo.items()))
