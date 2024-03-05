"""
Comparativa de tipos mutables e inmutables
Copia de objetos mutables
Inmutables: tuplas, cadenas (str)
Mutables: listas, conjuntos y diccionarios
"""

# Ordenar una lista:
L = [1,4,5,3,1,1]
print(L)
L.sort() # Cambia el objet
print(L)

# Convertir una cadena a mayúsculas: OJO no cambia el 
# objeto devuelve una copia
cad = "hola que tal"
print(cad)
cad.upper()
print(cad)

# Guardando una copia:
cad = "hola que tal"
print(cad)
cad2 = cad.upper()
print(cad2)