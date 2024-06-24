"""
Definición de listas:
- funciones
"""

L = [12, 4, 33, 55, 1]
print(L, type(L))
print("Suma: ", sum(L))
print("Recuento: ", len(L))
print("Promedio: ", sum(L) / len(L))
print("Máximo: ", max(L))
print("Mínimo: ", min(L))

# Acceso a los elementos de la lista
print("EL primero: ", L[0], L[-5])
L[-1] = 100
print(L)

# Recorrer la lista con un for:
for i in L:
    print(i, round(i * 0.21, 2))

# Añadir elementos a una lista:
L = [1, 2, 3, 4, 5]
L.append(100)
L += [200]
L.insert(0, 1000)  # Es la posición 0 colocamos el 1000.
print(L)

# print("pos: 20 ", L[20]) ERROR, nos salimos de la lista.

# L += 300 son incompatibles list e int. ERROR

# Operadores de list: + * in

# Operadores relacionales: ==, <, <= ...
