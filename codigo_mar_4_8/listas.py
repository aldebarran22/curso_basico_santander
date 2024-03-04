"""
Listas en Python:
- Crear: [] o con list()
- Acceso a los elementos
- Operadores: +, *, in
- Funciones sobre listas
- Slicing
"""
cad = "Hola que tal"
L = list(cad)
print(L)

L2 = [1,2,3,4,5]
print(L2)

# Las listas se pueden modificar:
L2[0] = 400
print(L2)
print('EL último de la lista:', L2[4], L2[-1])
print('El primero de la lista: ', L2[0], L2[-5])

# Añadir elementos a la lista:
L2 += [120] # L2 = L2 + [120]
print(L2)

print([1,2,3]+[4,5,6])
print([1,2,3]*10)

print('L2',L2)
numero = 5
if numero in L2:
    print('existe')
else:
    print('no existe')

# Crear una lista vacia:
L = []  # L = list()
print(L)