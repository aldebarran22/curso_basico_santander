"""
Prácticas con listas de Python
"""

# SLICING: Sirve para listas, cadenas y tuplas:
# L[ini:fin-1:salto=1]
L = [10, 20, 30, 40, 50, 60, 70, 80]
print("los 3 primeros: ", L[0:3])
print("los 3 primeros: ", L[:3])
print("los 3 últimos: ", L[-3:])
print("Quitar el primero y el último: ", L[1:-1])
print("Toda la lista de dos en dos: ", L[::2])
print("invertida: ", L[::-1])

cad = "acurruca"
if cad == cad[::-1]:
    print("Es un palíndromo")
else:
    print("no lo es")

numero = 12344321
if type(numero) == int:
    cad2 = str(numero)
    if cad2 == cad2[::-1]:
        print("Es un capicua")
    else:
        print("no lo es")
else:
    print("Se necesita un número entero")

# range(ini, fin-1, salto=1)

print(list(range(10)))
print(list(range(10, 0, -1)))
print(list(range(0, 101, 5)))

for i in range(20):
    print(i, end=" ")

