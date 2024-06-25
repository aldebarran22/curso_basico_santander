"""
Prácticas con listas de Python
"""

# SLICING: Sirve para listas, cadenas y tuplas:
# L[ini:fin-1:salto=1]
L = [10, 20, 30, 40, 50, 60, 70, 80]
print("los 3 primeros: ", L[0:3])
print("los 3 primeros: ", L[:3])
print('los 3 últimos: ', L[-3:])
print('Quitar el primero y el último: ', L[1:-1])
print('Toda la lista de dos en dos: ', L[::2])
print('invertida: ', L[::-1])



