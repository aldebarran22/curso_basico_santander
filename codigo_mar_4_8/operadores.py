"""
Pruebas con operadores aritméticos
"""

import math

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
print(
    f"Billetes de {billete} para el importe: {importe} son {numBilletes50}, resto: {restante}"
)

# Traducir la fórmula de la Ec. de 2º grado:
# ax^2 + bx + c = 0

a, b, c = 1, 5, 4  # 1,5,4
raiz = b**2 - 4 * a * c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2 * a)
    x2 = (-b - math.sqrt(raiz)) / (2 * a)
    print("x1", x1, "x2", x2)
else:
    print("no hay solución")
