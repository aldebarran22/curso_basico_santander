"""
Ordenar colecciones en Python
- Para listas: método sort
- Para otras colecciones: función sorted
 (devuelve una lista ordenada con los datos de la colección)
"""

L = ["Miguel", "Juan", "Andrea", "Sara", "Ana", "Alberto"]
L.sort()
print(L)
# Ordenar por la longitud del nombre:
L.sort(key=len)
print(L)

t = (45, 3, 11, 23, 67, 88, 90)
R = sorted(t, reverse=True)
print(t)
print(R)
