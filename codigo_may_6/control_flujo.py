"""
Control de flujo en Python:
- bucle while
"""

"""
# Bucle infinito
while True:
    pass
"""

# Leer un valor de teclado y solo se aceptan
# multiplos de 10:
while True:
    cadNumero = input("Teclear importe:> ")
    if cadNumero.isnumeric():
        numero = int(cadNumero)

        if numero % 10 != 0:
            print("Solo se aceptan multiplos de 10")
        else:
            break
    else:
        print(f"El número: {cadNumero} no es correcto")
