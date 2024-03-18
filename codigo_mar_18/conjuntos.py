"""
Conjuntos en Python:
crear, recorrer, operadores, quitar repetidos
"""

c1 = {5,7,8,8,7,2,1,2,4}
c1.add(8)
print(c1, type(c1))

# Quitar repetidos a un lista:
L = [4,5,6,2,1,2,1,2,4,5,6,7,8,8]
L2 = list(set(L))
print(L2)

comida = {"Sara", "Jorge","Ana", "Juan", "Miguel"}
cena = {"Ana", "Raúl","Alberto", "María","Miguel"}

print('Quien va a comer y a cenar: ', comida & cena)  # intersección
print('Quien va solo a comer: ', comida - cena) # Diferencia de conjuntos
print('Quien va solo a cenar: ', cena - comida)