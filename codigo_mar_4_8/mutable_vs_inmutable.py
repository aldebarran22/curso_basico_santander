"""
Comparativa de tipos mutables e inmutables
Copia de objetos mutables
Inmutables: tuplas, cadenas (str)
Mutables: listas, conjuntos y diccionarios
"""

# Ordenar una lista:
L = [1, 4, 5, 3, 1, 1]
print(L)
L.sort()  # Cambia el objeto
print(L)

# Convertir una cadena a mayúsculas: OJO no cambia el
# objeto devuelve una copia
cad = "hola que tal"
print(cad)
cad.upper()
print(cad)
print()

# Guardando una copia:
cad = "hola que tal"
print(cad, id(cad))
cad2 = cad.upper()
print(cad2, id(cad2))

# modificar el objeto: mutable ok!
L[0] = 1000

# modificar el objeto: inmutable error!
# cad[0] = 'X'

# Copiar objetos mutables: list, dict y set
L1 = [1, 2, 3, 4, 5]
L2 = L1  # Crea una referencia a los mismos datos
L1[0] = 1000
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print("-" * 20)

L1 = [1, 2, 3, 4, 5]
L2 = L1.copy()  # Copia: funciona bien si los elementos son inmutables
L1[0] = 1000
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print("-" * 20)

# Copiar una lista de listas
L1 = [[1, 2], [3, 4, 5]]
print(L1[0])
L2 = L1.copy()  # OJO, se comparten los elementos:
L1[0] = 1000
L1[-1].append(999)
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print("-" * 20)

# Copia profunda:
import copy
L1 = [[1, 2], [3, 4, 5]]
L2 = copy.deepcopy(L1)  # Genera una copia independiente
L1[0] = 1000
L1[-1].append(999)
print("L1", L1, id(L1))
print("L2", L2, id(L2))
print("-" * 20)