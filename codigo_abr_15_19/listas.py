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

cad = "hola que tal"
L3 = list(cad)
print(L3)

L4 = [5]

# Acceso a los elementos:
print(L)
print(L[3])
L[0] = 1000
print(L)

L += [2000] # L = L + [2000]
print(L)

# Crear Listas vacías:
L1 = []
L2 = list()

if not L1:
    print('L1 es vacía')
else:
    print('L1 tiene elementos')

# Dadas dos listas:
L1 = [1,2,3,4,4,2,31,6,7,8]
L2 = [8,9,0,1,2,34,3,4,4]
# Obtener otra lista con los valores comunes (sin repetidos)
R = [] 


