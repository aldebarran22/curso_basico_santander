"""
Tipos básicos: números, boolean, None
Son inmutables
"""

# numeros: int, float, complex
n1 = 10
n2 = 2.5
resul = n1 + n2
print(resul, type(resul))

# El resultado será complex
resul2 = 10 * 2.5 + (8 + 7j)
print(resul2, type(resul2))

# Convertir de texto a número:
numero = "1234.99"
numero2 = '456.67'
resul = numero + numero2
print("resul:",resul)
num1 = float(numero)
num2 = float(numero2)
resul = num1 + num2
print("resul:",resul)



