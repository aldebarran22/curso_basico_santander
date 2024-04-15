"""
Crear listas
Funciones sobre listas
Recorrer listas con bucles: for
Operadores: + * in
Función list
Acceso a los elementos
modificar elementos
Slicing
copiar listas
"""

L = [45, 12, 34, 77, 9]
print(L, type(L))
print('Suma: ', sum(L))
print('Recuento: ', len(L))
print('min: ', min(L))
print('max: ', max(L))
print('Promedio: ', sum(L)/len(L))

# Listas de múltiples tipos:
L2 = [True, 123, 8.99, "hola", [12,34]]

# Recorrer una lista:
for i in L:
    print(i)

for t in enumerate(L):
    print(t)

# Operadores: + * in
print([12,34] + [45,77])
print([12,34] * 7)
if 34 in L:
    print('El 34 está en L')
else:
    print('No está')