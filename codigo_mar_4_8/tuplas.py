"""
Tuplas en Python
- inicializar múltiples variables
- intercambiar variables
- paso de parámetros a funciones
- resultados de una consulta a la BD
- select * from clientes where pais = ? ('España',)
- llamada a funciones ...
- operadores: +, *, in
- Slicing, indices + / -
"""

t = (1, 2, 3, 4)
t2 = 5, 6, 7, 8

print(t, type(t))
print(t2, type(t2))

t3 = tuple('hola que tal')
print(t3)
print('los 3 últimos: ', t3[-3:])
print('a' in t3)

