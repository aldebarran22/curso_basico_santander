"""
Incluye la validación del importe tecleado
"""

# División entera: calcular el número de billetes necesarios de 50
# para sacar 240 euros

# Almacena los resultados en un diccionario:
billetes = [100, 50, 20, 10]
desgloseBilletes = dict()  # Crear un dict vacio

while True:
    simporte = input("Teclear importe:>")
    if simporte.isnumeric():
        importe = int(simporte)
        if importe % 10 == 0:
            break
        else:
            print("El importe no es correcto")
    else:
        print('Solo se admiten números enteros')

for b in billetes:
    if importe >= b:
        numeroBilletes = importe // b
        importe = importe % b
        desgloseBilletes[b] = numeroBilletes
        # print(f"Billetes de {b} = {numeroBilletes}")

    if importe == 0:
        break

print("Desglose:", desgloseBilletes)
for billete, cuenta in desgloseBilletes.items():
    print(f"{cuenta} de {billete}")
