"""
Conjuntos en Python:
crear, recorrer, operadores, quitar repetidos
"""

c1 = {5,7,8,8,7,2,1,2,4}
print(c1, type(c1))

# Quitar repetidos a un lista:
L = [4,5,6,2,1,2,1,2,4,5,6,7,8,8]
L2 = list(set(L))
print(L2)
