"""
Partimos de dos listas con números y queremos obtener la intersección
en otra tercera lista.
L1 = [1,2,3,4,5,6,7,4,5,6]
L2 = [6,7,5,4,11,15]
R = [4,5,6,7] no puede tener repetidos
"""

L1 = [1, 2, 3, 4, 5, 6, 7, 4, 5, 6]
L2 = [6, 7, 5, 4, 11, 15]
# Crea una lista vacía
R = []  # R = list()

for i in L1:
    if i in L2 and i not in R:
        R += [i]
print(R)

# Solución 2: utilizando conjuntos &: intersección
c1 = set(L1)
c2 = set(L2)
print(list(c1 & c2))


