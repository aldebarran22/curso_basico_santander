"""
Ordenar listas con el método: sort
Función sorted para ordenar otras colecciones.
"""

L = [4, 5, 6, 71, 2, 3]
L.sort()
print(L)

comida = {"Ana", "Raúl", "Roberto", "Jose Antonio", "Sara", "Olga"}
L2 = sorted(comida)
print(L2)
print(comida)

# DESC:
L2 = sorted(comida, reverse=True)
print(L2)

# Ordenar por la longitud del nombre:
L2 = sorted(comida, key=len)
print(L2)

# Ordenar lista de tuplas según la suma:
L = [(1, 2000, 3), (900,), (10, 20, 50), (0, 0, 0, 1)]
L.sort(key=sum)
print(L)

L = [("Raúl", 55, 1.9), ("Ana", 34, 1.7), ("Roberto", 23, 1.86)]
L.sort(key=lambda t: t[1])  # ASC por Edad
print(L)
L.sort(key=lambda t: t[2], reverse=True)  # DESC por Altura
print(L)
