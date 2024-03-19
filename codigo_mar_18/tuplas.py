"""
Tuplas en Python
- Definir tuplas, 
- Acceso a los elementos
- Operadores: +, *, in
- count, index
- Sentencias SQL parametrizadas:
- select * from clientes where pais=?
"""

# Inicializar múltiples variables
a, b, c = 1, 2, 3

t1 = (1, 2, 3, 4, 5, 6)
t2 = 6, 5, 4, 3, 1
print(t1, type(t1))
print(t2, type(t2))

t3 = 8
print(t3, type(t3))

t3 = (None,)
print(t3, type(t3))

# t3[0] = 10 # Error no se puede modificar
t3 += (8,9,0)
print(t3)

# intercambio de variables:
a,b = b,a
print('a:', a, 'b:',b)
