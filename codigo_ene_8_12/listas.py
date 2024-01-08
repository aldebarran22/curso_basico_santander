"""
Crear listas, acceso a los elementos
slicing, funciones (de python), método
"""
L = [1, 3, -21, 3, 50]
print(L)

L2 = ["hola", 34, 5.7, True, [4, 5, 6]]
print(L2)

# Acceso a los elementos:
print("El primero:", L[0], L[-5])
print("El último: ", L[4], L[-1])

L[3] = 7
# L[-2] = 7
print(L)

# Funciones aplicadas a las listas:
print("suma:", sum(L))
print("min: ", min(L))
print("max: ", max(L))
print("recuento: ", len(L))
print("promedio:", sum(L) / len(L))

# Recorrido:
for i in L:
    print(i, end=" ")
print()  # Imprime un salto de linea: \n

# Recorrido imprimiendo el indice y el valor:
for ind, valor in enumerate(L):
    print(ind, valor)

# Crear listas con list:
L3 = list("hola que tal")
print(L3)

L4 = list(range(11))
print(L4)

# slicing: L[ini:fin-1:salto=1]
L = [1, 2, 3, 4, 5, 6, 7]
print("los 3 primeros:", L[0:3])
print("los 3 primeros:", L[:3])  # desde el principio
print("los tres últimos:", L[-3:])
print("Toda la lista de dos en dos:", L[::2])
print("Quitar el primero y el último:", L[1:-1])
print("Invertir la lista:", L[::-1])

L2 = [1, 2, 3, 5, 6, 5, 3, 2, 1]
if L2 == L2[::-1]:
    print("capicua")
else:
    print("no es capicua")

path = "C:/mis documentos/hojas/libro1.xlsx"
L = path.split("/") # Partir la cadena por la /
print(L)
fichero = L[-1]
print('fichero:', fichero)


# Copiar listas:
