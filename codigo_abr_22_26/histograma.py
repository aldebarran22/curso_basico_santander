"""
Histograma:
Lista: Almacenar valores con repeticiones
Conjunto: Extraer los valores sin repetidos
Diccionario: Un recuento de cada valor
"""

import random

n = 1000
L = []
histo = dict()
# El intervalo de números:
ini = 1
fin = 25

# Almacenar n números aleatorios en la lista L
for i in range(n):
    L.append(random.randint(ini, fin))
#print(L[:5])

# Quitar los repetidos y almacenarlos en un conjunto
numeros = set(L)
# print(numeros)

# Contar los valores del conjunto en la lista y almacenar
# en el diccionario (la clave -> el número), (el valor -> el recuento)
for i in numeros:
    histo[i] = L.count(i)

# Imprimir resultados:
for numero, cuenta in histo.items():
    print(f"{numero} se repite {cuenta} veces")
