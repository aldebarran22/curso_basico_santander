"""
Objetos mutables: list, set, dict
Inmutables: tuple, str, int, float, bool
"""

L = [1, 3, 4, 1, -8, 9, -34]
L.sort()
print(L)

cad = "hola"
print(cad.upper())  # Devuelve una copia de la cadena
print(cad)

# Se suele hacer:
cad = cad.upper()
print(cad)

# Cambiar el ; por la , en una cadena (objeto inmutable)
csv = "10248;WILMK;5;3;32,38;Finlandia"
print(csv)
csv = csv.replace(",", ".")  # Convertir el float a formato inglés
print(csv)
csv = csv.replace(";", ",")
L = csv.split(",")
print(L)
