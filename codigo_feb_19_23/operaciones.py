"""
Operaciones con tipos numéricos: int / float
"""

# Calcular la media de dos números:
n1 = 11
n2 = 56
media = (n1 + n2) / 2
print('media: ', media)

# Cuantos billetes de 50 € necesitamos para 230 €
numbilletes = 230 // 50
print('num Billetes de 50:',numbilletes)

cantidad = 230
billete = 50
numbilletes = cantidad // billete
resto = cantidad % billete
print(cantidad,'necesitamos',numbilletes,"de",billete)
#f-string
print(f"Para {cantidad} eur necesitamos {numbilletes} billetes de {billete}")
print('Nos quedan ',resto)
