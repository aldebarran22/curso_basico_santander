"""
Crear un histograma con un diccionario en Python
"""

L = [100, 200, 200, 100, 200, 200, 200, 500, 600, 300, 800]

# Cuantos valores distintos tenemos:
c = set(L)
print(c, type(c))
print("Cuantos valores distintos tenemos:", len(c))
histo = dict()
for i in c:
    histo[i] = L.count(i)

# Ordenar DESC por la cuenta:
R = sorted(histo.items(), key=lambda t: t[1], reverse=True)

for valor, cuenta in R:
    print(f"{valor} se repite {cuenta} veces")

print(histo.items())
