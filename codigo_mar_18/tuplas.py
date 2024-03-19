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
t3 += (8, 9, 0)
print(t3)
t3 = (5,)
print(t3)

# intercambio de variables:
a, b = b, a
print("a:", a, "b:", b)

t = (1, 2, 3, 4)
print(t * 4)
print(t + (8, 9, 0))
print("2 in t:", 2 in t)

# Métodos: count, index:
t = (1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 3, 4)
numero = 1
print(f"numero: {numero} se repite {t.count(numero)} veces")
print(f"La posición de {numero} en t: {t.index(numero)}")
print(f"La posición de {numero} en t: {t.index(numero, 1)}")
print(f"La posición de {numero} en t: {t.index(numero, 11)}")

t = (1, 2, 3, 4, 1, 6, 7, 8, 9, 1)
numero = 1
ini = 0
for i in range(t.count(numero)):
    pos = t.index(numero, ini)
    print(f" posicion de {numero} es {pos}  ")
    ini = pos + 1

# Expansión de tuplas:
fichero = "libro1.xlsx"
t = fichero.partition('.')
print(t)

nom, _, ext = fichero.partition('.')
print(nom)
print(ext)
ext = fichero.partition('.')[2]
print(ext)
