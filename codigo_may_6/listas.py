"""
Listas en Python:
- Crear listas: [], list()
- Acceso a los elementos con los índices
- Funciones: sum, len, min, max
- Operadores: +, *, in 
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
print("num letras: ", len(L3), len(frase))

# Añadir elementos a una lista:
L3 += ["X"]
print(L3, len(L3))
L3.insert(3, "A")
print(L3, len(L3))

# Append vs extend
L = [3,4,5,6,2,1,0]
L2 = [1,2,3]

L.append(L2)
L.append(10)
print(L)

L = [3,4,5,6,2,1,0]
L2 = [1,2,3]

L.extend(L2)
#L.extend(10) necesita un iterable
print(L)

# Operadores: 
L1 = [1,2,3]
L2 = [4,5,6]
print(L1 + L2)
print(L1 * 5)
print("2  in L1: ", 2 in L1)

# bucle for:
for i in L:
    print(i, end=" ")
print() # Salto de linea

# bucle for con índices:
for pos, i in enumerate(L):
    print(pos, i)

for i in range(10):
    print(i, end=" ")
print()

# Crear listas con list y range:
# range(ini, fin-1, salto=1)
L = list(range(10)) # del 0 al 9
print(L)
# del 1 al 10
L = list(range(1,10))
print(L)