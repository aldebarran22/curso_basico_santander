"""
Listas en Python:
- crear listas
- operadores: +, *, in
- índices + y -, slicing, 
- bucle: for
- funciones de uso general
- acceso a los elementos
- copia
""" 

L = [1,4,5,4,2,3,1]
L2 = [True, 123, [4,5,6], "hola"]
print(L, type(L))

L3 = list('hola que tal')
print(L3)

# Funciones de uso general:
L = [12, 33, 45, 77]
print('Recuento: ', len(L))
print('Suma: ', sum(L))
print('Media:', sum(L) / len(L))
print('minimo: ', min(L))
print('maximo: ', max(L))

# operadores: +, *, in
L1 = [1,2,3]
L2 = [4,5,6]
print(L1 + L2)
print(L1 * 5)
print("5 in L1:", 5 in L1)
print("2 in L1: ", 2 in L1)

# Añadir elementos a una lista:
R = []
R += [2]
R += [3,6,7,8]
print(R)

# Bucle for:
for i in R:
    print(i, end=' ')
print() # salto de línea

# Dadas dos listas obtener en otra lista los elementos comunes:
L1 = [1,2,3,4,3,2,1,1,2,7]
L2 = [1,2,7,8,9]
R = []
for i in L1:
    if i in L2 and i not in R:
        R += [i]
print(R)
