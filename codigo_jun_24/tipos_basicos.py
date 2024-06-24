"""
Pruebas con el tipado dinámicos.
Definir, imprimir variables
Ver el tipo de una variable
"""

numero = 100.5
print("numero:", numero, "tipo:", type(numero))

numero2 = 150
print("numero2:", numero2, "tipo:", type(numero2))
resul = numero + numero2
print("Resultado de suma:", resul)

resul = numero - numero2
print("Resultado de la resta: ", resul)

# Calcular el iva de un producto:
importe = 240.56
iva = round(importe * 0.21, 2)
print("importe:", importe, "iva:", iva)

# Calcular el promedio de dos variables:
num1 = 23
num2 = 56
media = (num1 + num2) / 2
print("promedio:", media)

# División entera: calcular el número de billetes necesarios de 50
# para sacar 240 euros
importe = 240
billetes50 = importe // 50
importe = importe % 50
print("bill de 50: ", billetes50)

billetes20 = importe // 20
importe = importe % 20
print("bill de 20: ", billetes20)

billetes10 = importe // 10
importe = importe % 10
print("bill de 10: ", billetes10)

"""
Prioridades de los operadores:
** potencia
* / // % 
+ -
"""
