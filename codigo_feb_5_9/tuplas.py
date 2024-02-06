"""
Tuplas en Python: 
- Inicializar múltiples variables
- Intercambiar variables
- Paso de parámetros a una función sin indicar el número
- En los resultados de una consulta a la base de datos
- Setencias parametrizadas:
- select * from clientes where pais=? ('España',)
"""

# Expansión de tuplas
a, b, c = 1, 2, 3

t = 1, 2, 3
t2 = (4, 5, 6)
print(t, t2, type(t), type(t2))

# Crear una tupla de un solo elemento:
t3 = (1,)
print(t3, type(t3))

a = 10
b = 20
a,b = b,a
print('a',a, 'b',b)

L = [('Ana',34,1.78),('Jorge',31,1.77),('Raúl',45, 1.79)]
for i in L:
    print(i[0])

# Expansión de tuplas:
for nombre,edad,altura in L:
    print(nombre)

# in, count, index:
t = (1,2,3,4,3,2,1,1,6,7,8)
print('10:',t.count(10))
print('1:',t.count(1))
print('index del 1:', t.index(1))
print('sig index del 1:', t.index(1, 1))

# Obtener las posiciones donde se encuentra el 1 en la tupla: t
ini = 0
n = t.count(1)
for i in range(n):
    pos = t.index(1, ini)
    print('pos: ', pos)
    ini = pos+1


