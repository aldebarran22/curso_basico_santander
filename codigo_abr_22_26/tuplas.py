"""
Tuplas:
- Crear tuplas

- Inicialización múltiple, expansión de tuplas
- Intercambio de variables
- Parámetros de una función: sin límite de parámetros
- SQL: sentencias parametrizadas: 
select * from clientes where pais=?

Operadores: + * in slicing
Métodos: count, index
"""

a, b, c = 3, 4, 5

a, b = b, a
print(a, b)

t = tuple(range(1, 11))
print(t)

t2 = (1, 2, 3, 1, 22, 3, 1, 2, 3, 1)
print(t2.index(1))
print(t2.index(1, 1))
print(t2.index(1, 4))

# Obtener las posiciones  que ocupa un valor dentro de la tupla
valor = 3
inicio = 0
n = t2.count(valor)
for i in range(n):
    pos = t2.index(valor, inicio)
    print(pos, end=' ')
    inicio = pos + 1
print()

## Expansión de tuplas en una lista:
L = [(40.4, -3.68), (42.5, -4.9), (38.6, -5.7)]
for t in L:
    print(f'latitud: {t[0]}, longitud: {t[1]}')
print()

for lat, lon in L:
    print(f'latitud: {lat}, longitud: {lon}')
