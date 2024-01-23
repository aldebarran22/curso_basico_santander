# Validación de números con 3 intentos posibles
intentos = 0
numero = 0
correcto = False
while True:
    intentos += 1
    snumero = input("Teclear importe:>")
    if snumero.isnumeric():
        numero = int(snumero)
        if numero % 10 == 0:
            correcto = True
            break
        else:
            print("Solo se aceptan múltiplos de 10")
    else:
        print("Solo aceptan números")

    if intentos == 3:
        print("Ha consumido los 3 intentos")
        break

if correcto:
    print("El importe es: ", numero)
