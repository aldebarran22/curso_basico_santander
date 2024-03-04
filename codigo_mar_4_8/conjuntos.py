"""
Conjuntos en Python:
- {}, set
- Quitar repetidos
- Operadores a nivel de conjuntos:
& intersección
| unión
- diferencia
^ diferencia simétrica
"""

# Quitar repetidos de una lista:
L = [1, 2, 3, 4, 5, 6, 7, 7, 8, 1, 2, 3, 7, 8]
c = set(L)
print(c)

c2 = {3, 3, 3, 2, 1, 2, 25, 6, 6, 7, 8, 9, 0}
print(c2, type(c2))

# Quitar repetidos de una lista y dejar el resultado en otra lista:
L2 = list(set(L))
print(L2)

comida = {"Sonia","Alberto","Ana", "Marta","Andrés"}
cena = {"Ana","Raúl","Alberto", "Miguel", "Sara"}



