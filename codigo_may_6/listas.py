"""
Listas en Python:
- Crear listas: [], list()
- Acceso a los elementos con los índices
- Funciones: sum, len, min, max
- Slicing
- Bucles
- Copia de listas
"""

L = [12, 33, 1, 90, 120, 12]
print(L, type(L))
print("suma: ", sum(L))
print("recuento: ", len(L))
print("max:", max(L))
print("min:", min(L))
print("promedio: ", sum(L) / len(L))

# Acceso a los elementos:
print(L[3], L[-3])
L[5] = -5
print(L)

# Listas mixed:
L2 = ["hola", 34, True, [1, 2, 3], 5.77]
print("El 2: ", L2[3][1])

# Crear listas con list()
frase = "hola que tal"
L3 = list(frase)
print(L3)
