"""
Tuplas en Python.
- Inicializar múltiples variables
- Intercambiar variables
- Expansión de tuplas
- Paso de parámetros a funciones
- Para almacenar registros de una consulta a la BD.
- select * from clientes where pais=? ("España",)
- Operadores: + * in slicing, indices + y -
- No se modificar una tupla
"""

t = 1, 2, 3, 4
t2 = (5, 6, 7, 8)
print(t, type(t))

t = 1
print(t, type(t))

t = (1,)
print(t, type(t))

# inicializar variables:
a, b, c = 1, 2, 3

t = 1, 2, 3
a, b, c = t

L = [(40.2, -3.65), (42.6, -2.7), (55.5, 12.5)]
for t in L:
    print(t[0],t[1])

for lat, lon in L:
    print(lat, lon)


t2 += (8,9,10) # t2 = t2 + (8,9,10)
print(t2)
#t2[0] = 1000

# index y count:
t = (1,3,4,2,3,5,6,7,1,2,1)
# imprimir las posiciones que ocupa un numero en la tupla
numero = 1
ini = 0
for i in range(t.count(numero)):
    pos = t.index(numero, ini)
    print(pos)
    ini = pos + 1
