"""
Ordenar listas con el método: sort
Función sorted para ordenar otras colecciones.
"""

L = [4,5,6,71,2,3]
L.sort()
print(L)

comida = {"Ana", "Raúl", "Roberto", "Jose Antonio" "Sara", "Olga"}
L2 = sorted(comida)
print(L2)
print(comida)

# DESC:
L2 = sorted(comida, reverse=True)
print(L2)

# Ordenar por la longitud del nombre:
L2 = sorted(comida, key=len)
print(L2)
