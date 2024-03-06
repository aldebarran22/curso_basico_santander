"""
Generar un histograma a partir de una lista con
elementos repetidos
"""

cad = "Generar un histograma a partir de una lista con elementos repetidos"
L = list(cad)
letras = set(L)
histo = dict()
for letra in letras:
    histo[letra] = L.count(letra)

R = sorted(histo.items(), key=lambda t: t[1], reverse=True)
# Lord = sorted(histo.items(), key=)

for letra, cuenta in R:
    print(letra, cuenta)

