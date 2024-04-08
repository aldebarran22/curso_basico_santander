"""
Tipos básicos
"""

resul = 12 + 7.88
print(resul, type(resul))

resul = 12 + 7.88 + 6 + 8j
print(resul, type(resul))

# Tipo Boolean
# En python es False: 0, "" cadena vacía, [] lista vacía, None (algo vacío)
numero = 0
if numero:
    print('numero != 0')
else:
    print('numero es cero')

n1 = 10
n2 = 20
suma = n1 + n2
print(n1,'+',n2,'=',suma)

#f-string >= python 3.6
print(f"{n1} + {n2} = {suma}")

# Calcular la media de dos números: div. real
n1 = 5
n2 = 8
print(f'media: {(n1 + n2) / 2}')

# Calcular el número de billetes de 50 para un importe de 230
importe = 230
numBilletes = importe // 50
print('num billetes: ', numBilletes, ' el resto:', importe % 50)
