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
