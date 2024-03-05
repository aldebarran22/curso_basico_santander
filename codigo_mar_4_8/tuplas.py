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
print(t3 + t)
print((1,2)*3)

L = [(40.4, -3.68), (34, -77), (45.6, -12), (-45, 77)]
print(L[0][0])
print('len:',len(L))
for t in L:
    print(t)

# Desempaquetar/expandir tuplas
for lat, lon in L:
    dirLat = 'N' if lat > 0 else 'S'
    dirLon = 'E' if lon > 0 else 'W'
    print(f"{lat}{dirLat}, {lon}{dirLon}")

