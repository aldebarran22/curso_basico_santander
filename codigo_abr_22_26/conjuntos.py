"""
Conjuntos en Python:
- Quitar repetidos
- Creación
- Añadir elementos
- Operadores: & | - ^
"""

c = {1,1,1,2,3,1,2,6}
print(c, type(c))

L = [1,2,3,4,3,1,2,3,4,5,6,7,1,2,7]
c2 = set(L)
print(c2)

L2 = list(set(L))
print(L2)