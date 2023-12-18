"""
Comparativa entre un tipo mutable (lista)
y un tipo inmutable (str)
"""

# Uso de un tipo inmutable
nombre = "Ana Maria"
print(nombre.upper())
nombre.upper()
print(nombre)

# Uso de un tipo mutable
L = [4,6,3,1,2,-9]
L.sort()
print(L)
