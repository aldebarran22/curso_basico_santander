
# División entera: calcular el número de billetes necesarios de 50
# para sacar 240 euros
importe = 40
billetes50 = importe // 50
importe = importe % 50
print("bill de 50: ", billetes50)

billetes20 = importe // 20
importe = importe % 20
print("bill de 20: ", billetes20)

billetes10 = importe // 10
importe = importe % 10
print("bill de 10: ", billetes10)