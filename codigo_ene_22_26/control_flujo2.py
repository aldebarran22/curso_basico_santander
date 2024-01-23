# Validación de números con 3 intentos posibles
intentos = 0
while True:
    intentos += 1
    snumero = input("Teclear importe:>")
    if snumero.isnumeric():
        numero = int(snumero)
        if numero % 10 == 0:
            break
        else:
            print("Solo se aceptan múltiplos de 10")
    else:
        print("Solo aceptan números")

    if intentos == 3:
        print("Ha consumido los 3 intentos")
        break

if numero % 10 == 0:
    print("El importe es: ", numero)
