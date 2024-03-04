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