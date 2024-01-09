"""
Definición de conjuntos, quitar repetidos, buscar elementos coincidentes..
"""
L = [100, 34, 45, 34, 200, 200, 67, 90, 45, 34, 200]
c = set(L)
print(c, type(c))

comida = {"Raquel", "José", "Miguel", "Sandra", "Jorge"}
cena = {"Eva", "Miguel", "Sandra", "Nuria", "Juan"}

print("Quien va a comer y a cenar: ", comida & cena)
print("Quien va solo a comer:", comida - cena)
print("Quien va solo a cenar:", cena - comida)
print("Quienes han participado en los eventos:", comida | cena)
print("Quienes se han apuntado a un solo evento:", comida ^ cena)
