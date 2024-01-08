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
print('El último: ', L[4], L[-1])

L[3] = 7
# L[-2] = 7
print(L)

# Funciones aplicadas a las listas:
print('suma:', sum(L))
print('min: ', min(L))
print('max: ', max(L))
print('recuento: ', len(L))
print('promedio:', sum(L)/len(L))

# Recorrido:
for i in L:
    print(i, end=' ')
print() # Imprime un salto de linea: \n

# Recorrido imprimiendo el indice y el valor:
for ind, valor in enumerate(L):
    print(ind, valor)
