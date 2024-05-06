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
L = [3, 4, 5, 6, 2, 1, 0]
L2 = [1, 2, 3]

L.append(L2)
L.append(10)
print(L)

L = [3, 4, 5, 6, 2, 1, 0]
L2 = [1, 2, 3]

L.extend(L2)
# L.extend(10) necesita un iterable
print(L)

# Operadores:
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1 + L2)
print(L1 * 5)
print("2  in L1: ", 2 in L1)

# bucle for:
for i in L:
    print(i, end=" ")
print()  # Salto de linea

# bucle for con índices:
for pos, i in enumerate(L):
    print(pos, i)

for i in range(10):
    print(i, end=" ")
print()

# Crear listas con list y range:
# range(ini, fin-1, salto=1)
L = list(range(10))  # del 0 al 9
print(L)
# del 1 al 10
L = list(range(1, 11))
print(L)
# del 0 al 100 de 5 en 5
L = list(range(0, 101, 5))
print(L)
# del 10 al 1
L = list(range(10, 0, -1))
print(L)
print(range(10))

# Slicing: L[ini:fin-1:salto=1]
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("los 3 primeros:", L[0:3])
print("los 3 primeros:", L[:3])
print("los 3 últimos:", L[-3:])
print("Toda la lista:", L[:])
print("Toda la lista de 2 en 2:", L[::2])
print("invertir: ", L[::-1])

# Es palíndromo:
cad = "acurruca"
if cad == cad[::-1]:
    print("es un palíndromo")
else:
    print("no lo es")

num = 12344321
snum = str(num)
if snum == snum[::-1]:
    print("es capicua")

path = "C:/onedrive/documents/libro1.xlsx"
L = path.split("/")
print(L[-1])

# Extraer los valores en común de dos listas:
L1 = [1, 3, 4, 5, 6, 1, 2, 3]
L2 = [5, 8, 9, 5, 1, 0, 5]
R = []  # R = list()
for i in L1:
    if i in L2 and i not in R:
        R.append(i)  # R += [i]
print(R)

# print(R[10]) Excepción IndexError, nos salimos con el índice
