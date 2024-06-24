# División entera: calcular el número de billetes necesarios de 50
# para sacar 240 euros
billetes = [50,20,10]
importe = int(input("Teclear importe:>"))
if importe % 10 == 0:
    for b in billetes:
        if importe >= b:
            numeroBilletes = importe // b
            importe = importe % b
            print(f"Billetes de {b} = {numeroBilletes}")
else:
    print("El importe no es correcto")
