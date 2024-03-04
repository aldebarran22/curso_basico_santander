"""
Pruebas con operadores aritméticos
"""

# Calcular la media de dos números:
n1 = 123
n2 = 900
media = (n1 + n2) / 2
print("media: ", media)
# f-string
print(f"La media de {n1} y {n2} es {media}")

# Cuanto billetes de 50 necesito para desglosar 230 euros
importe = 230
billete = 50
numBilletes50 = importe // billete
restante = importe % billete
print(f"Billetes de {billete} para el importe: {importe}, resto: {restante}")
