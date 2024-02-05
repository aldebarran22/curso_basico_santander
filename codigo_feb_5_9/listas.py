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
# print('fuera del bucle')

for pos, i in enumerate(L):
    print(pos, i)

# Comprobar si el valor 15 está en la lista:
numero = 7
if numero in L:
    print(numero, "está en la lista")
    print("La pos es: ", L.index(numero))
    print("Se repite: ", L.count(numero), "veces")
else:
    print(numero, "no está")

# Slicing: vale para list, tuple y str
# variable[inicio:fin-1:salto=1]
print(L)
print("los tres primeros: ", L[0:3])
print("los tres primeros: ", L[:3])  # desde el inicio
print("los 3 últimos:", L[-3:])  # hasta el final de la lista
print("Quitar el primero y el último:", L[1:-1])
print("Elementos de dos en dos: ", L[::2])  # desde el principio hasta el final
print("Invertir: ", L[::-1])

# Comprobar si una cadena es un palíndromo
s = "arenera"
if s == s[::-1]:
    print(s, "es un palíndromo")
else:
    print("no lo es")

prefijo = "ana"
n = len(prefijo)
L = ["ana", "anabel", "ana maria"]
for nombre in L:
    if prefijo in nombre:
        print(nombre[n:])

# Modificar elementos de una lista:
L = [3, 4, 5, 6, 7]
print(L)
L[0] = 30  # Machaca el valor de la posición 0
L[-1] *= 2  # Duplica el último valor
print(L)


nombre = "ana"
# Intento modificar la primera letra:
# nombre[0] = 'A' No se puede modificar --> inmutable

# Añadir elementos a una lista:
print(L)
L += [500, 600, 700]
print(L)

# + y *

# range(ini, fin-1, salto=1)
print("Del 0 al 9:", list(range(10)))
print(list(range(0, 101, 5)))
print("Cuenta atrás: ", list(range(10, 0, -1)))

# Ejecutar un bucle 10 veces!
for i in range(10):
    print(i, end=" ")
print()  # Salta de línea
