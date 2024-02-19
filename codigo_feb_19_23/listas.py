"""
Listas en Python
"""

L = [1, 2, 3, 5, -1, 12]
print(L, type(L))
print("suma:", sum(L))
print("minimo:", min(L))
print("maximo:", max(L))
print("Recuento: ", len(L))
print("Promedio: ", sum(L) / len(L))

# Acceso a los elementos
print("El primero: ", L[0])
L[1] = 300
print(L)
# print(L[7]) Nos salimos fuera de la lista
L2 = [True, 123.88, ["e", "f", "h"], 12, "hola"]
print("La primera letra del segundo elemento: ", L2[2][0])
L2[2][0] = False
print(L2)
L2[2] = 0
print(L2)


# Añadir elementos:
L = [1, 2, 3, 5, -1, 12]
L += [100]  # L = L + [100]
L.append(200)
print(L)
L.insert(0, 25)
print(L)
L.insert(2, 33)
print(L)
aux = [1, 2, 3]
# L.append(aux)
L.extend(aux)
print(L)

# in: para saber si un elemento está o no dentro de la lista:
numero = 99
if numero in L:
    print(f"{numero} está en la lista")
else:
    print(f"{numero} no está en la lista")

# bucle,
for i in L:
    print(i, end=" ")
print() # salto de linea

# slicing, índices negativos
L = [1,2,3,5,-1,12]
print('El primero:',L[0], L[-6])
print('El último: ', L[-1], L[5])
# slicing: L[ini:fin-1:salto=1]
print('los 3 primeros:', L[0:3])
print('los 3 primeros:', L[:3])
print('quitar el último:', L[:-1])
print('los 3 últimos:',L[-3:])
print('quitar primero y último:',L[1:-1])
print('toda la lista: ', L[:])
print('toda la lista de dos en dos: ', L[::2])
print('invertida: ', L[::-1])

path = "C:/mis documentos/excel/libro1.xlsx"
L = path.split("/")
print(L[-1])

cad = "ana"
if cad == cad[::-1]:
    print('es un palindromo')
else:
    print('no lo es')