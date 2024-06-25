"""
Operaciones con conjuntos en Python.
- Quitar repetidos
- operadores:
& intersección
| unión
- diferencia
^ diferencia simétrica
"""

c = {1, 2, 32, 1, 1, 2, 3, 4, 1}
print(c, type(c))

L = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]
c2 = set(L)
print(c2)

cad = "hola que tal estas hoy"
c3 = set(cad)
print(c3)

# print(c3[0]) el conjunto no es indexable!
