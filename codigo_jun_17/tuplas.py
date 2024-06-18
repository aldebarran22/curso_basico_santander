"""
Tuplas: definición
Operadores (+ * in) y slicing, for: igual que en las listas
Indices: positivos y negativos
- Paso de parámetros a funciones
- intercambiar variables
- SQL: select * from clientes where pais='Alemania'
- select * from clientes where pais = ? and importe > ? ("Alemania", 1000)
- [("Alemania", 1000), ("Francia",56)]
"""

import os

t1 = 1, 2, 3, 4
t2 = (5, 6, 7, 8)
print(t1, type(t1))

t3 = ("Alemania",)
print(t3, type(t3))

# Intercambiar variables:
ini = 50
fin = 10
print(ini, fin)
ini, fin = fin, ini
print(ini, fin)

gps = [(40.4, -3.65), (42.6, 5.7), (36.7, 1.6)]
for t in gps:
    print(t[0], t[1])

# Expansión de tuplas:
for lat, lon in gps:
    print(lat, lon)


ficheros = os.listdir()
for fich in ficheros:
    nombre, _, ext = fich.partition(".")
    if ext == 'ipynb':
        print(fich)

