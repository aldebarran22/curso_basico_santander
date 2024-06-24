"""
Prácticas sobre listas:
"""

L = [78, 1, 2, 3, 5, 6, 5, 4, 112, 2, 4, 5, 6]
# filtrar valores > 50
R = []
for i in L:
    if i > 50:
        R.append(i)

print(R)

# filtrar valores > 50 sin repetidos
L = [78, 1, 2, 78, 5, 106, 5, 4, 112, 112, 4, 5, 6]
R = []
for i in L:
    if i > 50 and i not in R:
        R.append(i)

print(R)

# Dada una lista crear dos listas una con los
# números pares y otra con los impares
L = [2, 4, 6, 5, 15, 6, 3, 2, 17, 8, 9, 11]
I = []
P = []
for i in L:
    if i % 2 == 0:
        P.append(i)
    else:
        I.append(i)

print(I)
print(P)

# Crear listas con list:
frase = "hola que tal"
L2 = list(frase)
print(L2)
L3 = frase.split(" ")
print(L3)

emp = "1;Davolio;Representante de ventas"
Lemp = emp.split(";")
print(Lemp)
print(Lemp[1])