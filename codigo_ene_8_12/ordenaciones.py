"""
Ordenar colecciones con distintos criterios
Uso de funciones lambda
"""
L = ["Beatriz", "ana", "Miguel", "Jose", "alberto"]
L.sort()
print(L)
L.sort(key=str.capitalize)
print(L)

L2 = [-6, 0, -11, 123, 90, 56]
L2.sort() # ASC
print(L2)
L2.sort(reverse=True) # DESC
print(L2)

t = (-6, 0, -11, 123, 90, 56)
t2 = tuple(sorted(t))
print(t2)

L = [('Sara', 34), ('Miguel',56), ('Andrés',23), ('Ana',33), ('Jorge',6)]
L.sort() # Por defecto ordena por el primer campo de la tupla
print(L)
L.sort(key=lambda t : t[1])
print(L)
