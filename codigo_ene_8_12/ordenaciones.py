"""
Ordenar colecciones con distintos criterios
Uso de funciones lambda
"""
L = ["Beatriz", "ana", "Miguel", "Jose", "alberto"]
L.sort()
print(L)
L.sort(key=str.capitalize)
print(L)
