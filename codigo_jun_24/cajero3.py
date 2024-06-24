# División entera: calcular el número de billetes necesarios de 50
# para sacar 240 euros

# Almacena los resultados en un diccionario:
billetes = [100, 50, 20, 10]
desgloseBilletes = dict()  # Crear un dict vacio
importe = int(input("Teclear importe:>"))
if importe % 10 == 0:
    for b in billetes:
        if importe >= b:
            numeroBilletes = importe // b
            importe = importe % b
            desgloseBilletes[b] = numeroBilletes
            # print(f"Billetes de {b} = {numeroBilletes}")

        if importe == 0:
            break

    print("Desglose:", desgloseBilletes)
else:
    print("El importe no es correcto")
