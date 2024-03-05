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

for letra, cuenta in histo.items():
    print(letra, cuenta)

