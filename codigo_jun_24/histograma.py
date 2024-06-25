"""
Generar un histograma con una lista de valores aleatorios.
"""

import random

N = 1000

# Generar una lista con N números aleatorios:
L = []
for i in range(N):
    L.append(random.randint(1,20))

print(L[:10])
