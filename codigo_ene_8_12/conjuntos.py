"""
Definición de conjuntos, quitar repetidos, buscar elementos coincidentes..
"""
L = [100, 34, 45, 34, 200, 200, 67, 90, 45, 34, 200]
c = set(L)
print(c, type(c))

comida = {"Raquel", "José", "Miguel", "Sandra", "Jorge"}
cena = {"Eva","Miguel", "Sandra", "Nuria","Juan"}

print('Quien va a comer y a cenar: ', comida & cena)

