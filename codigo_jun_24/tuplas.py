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
