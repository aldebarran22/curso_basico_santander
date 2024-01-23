"""
Bucles y condiciones en Python.
Bucles infinitos, break y continue
"""
# if compacto
numero = 20
print("par" if numero % 2 == 0 else "impar")

# Lo mismo: con if else
if numero % 2 == 0:
    print("par")
else:
    print("impar")

# Bucle while: imprimir del 1 al 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Validación de teclado: sólo acepta múltiplos de 10
"""
numero = int(input("Teclear importe:>"))
intento = 1
while numero % 10 != 0 and intento < 3:
    print("Sólo se aceptan múltiplos de 10")
    numero = int(input("Teclear importe:>"))
    intento += 1
if numero % 10 == 0:
    print("El importe es: ", numero)
else:
    print("ha consumido los 3 intentos")
"""

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
