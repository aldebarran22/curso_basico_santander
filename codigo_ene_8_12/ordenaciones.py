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
