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
R += [3]
print(R)