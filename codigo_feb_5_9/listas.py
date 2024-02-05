"""
Listas en Python.
Definición, acceso a los elementos
índices, funciones ...
"""

L = [3, 4, 5, 6, 7]
print(L, type(L))
print("suma: ", sum(L))  # funcion(variable)
print("recuento:", len(L))
print("minimo:", min(L))
print("maximo:", max(L))
print("promedio:", sum(L) / len(L))

nombre = "Ana"
print(len(nombre))

# Acceso a los elementos de la lista:
print(L)
print("El primero de la lista:", L[0])
print("El primero de la lista:", L[-5])
print("El último de la lista:", L[-1])
print("El último de la lista:", L[4])

path = "C:/mis documentos/excel/Libro1.xlsx"
L2 = path.split("/")
print(L2)
print("Fichero:", L2[-1])

# Recorrer una lista: con un bucle for
for i in L:
    print(i)
#print('fuera del bucle')
    
for pos, i in enumerate(L):
    print(pos, i)

# Comprobar si el valor 15 está en la lista:
numero = 7
if numero in L:
    print(numero,'está en la lista')
else:
    print(numero, 'no está')



