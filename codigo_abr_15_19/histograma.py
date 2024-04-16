"""
Crear un histograma con un diccionario en Python
"""

L = [100, 200, 200, 100, 200, 200, 200, 500, 600, 300, 800]

# Cuantos valores distintos tenemos:
c = set(L)
print(c, type(c))
print('Cuantos valores distintos tenemos:', len(c))
histo = dict()
for i in c:
    histo[i] = L.count(i)
    
