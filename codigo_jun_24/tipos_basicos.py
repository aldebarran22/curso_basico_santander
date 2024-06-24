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
print("importe:", importe,'iva:',iva)
