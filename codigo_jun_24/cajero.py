# División entera: calcular el número de billetes necesarios de 50
# para sacar 240 euros
importe = int(input("Teclear importe:>"))
if importe % 10 == 0:
    billetes100 = importe // 100
    if billetes100 > 0:
        importe = importe % 100
        print("bill de 100: ", billetes100)

    billetes50 = importe // 50
    if billetes50 > 0:
        importe = importe % 50
        print("bill de 50: ", billetes50)

    billetes20 = importe // 20
    if billetes20 > 0:
        importe = importe % 20
        print("bill de 20: ", billetes20)

    billetes10 = importe // 10
    if billetes10 > 0:
        importe = importe % 10
        print("bill de 10: ", billetes10)
else:
    print("El importe no es correcto")
