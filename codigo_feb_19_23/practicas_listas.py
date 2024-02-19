"""
Dadas dos listas: L1, L2 calcular los números
comunes.
"""

L1 = [3, 4, 2, 1, 2, 3, 4, 6, 8, 5]
L2 = [4, 6, 5, 0, 9, 10, 11, 8]
R = []
for i in L1:
    if i in L2 and not i in R:
        R.append(i)
print(R)
