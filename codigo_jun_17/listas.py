"""
Listas: definión, constructor list()
acceso a los elementos
bucles
funciones
...
"""

L = [23,11,6,-6,10]
print('Recuento: ', len(L))
print('Suma: ', sum(L))
print("Promedio: ", sum(L) / len(L))
print('Mínimo: ', min(L))
print('Máximo: ', max(L))
print('El primero: ', L[0], L[-5])

# Indices + y - (funciona igual en: listas, tuplas y cadenas)
L2 = [[1,2,3,4], [5,6,7,8]]
print("len de L2: ", len(L2))
print("El primero: ", L2[0])
print('El primero del primero: ', L2[0][0])
print('El ocho: ', L2[-1][-1])


# Operadores: + * in (funciona igual en: listas, tuplas y cadenas)
L1 = [10,20,30]
L2 = [4,5,6]
print(L1 + L2) # concatena
print(L1 * 5) # concatena 5 veces
num = 3
if num in L1:
    print(f'num: {num} está en la lista')
else:
    print('no está')

# Bucle:
for i in L1:
    print(i)

# Bucle con los índices:
for pos, i in enumerate(L1):
    print(pos, i)


# Slicing: L[ini:fin-1:salto=1] (funciona igual en: listas, tuplas y cadenas)
L = [1,2,3,4,5,6,7,8]
print(L, type(L))

# Los tres primeros:
print('los 3 primeros: ', L[0:3])
print('los 3 primeros: ', L[:3])

print('los 3 últimos: ', L[-3:])
print('quitar el primero y el último: ')


