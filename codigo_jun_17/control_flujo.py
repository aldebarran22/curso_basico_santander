"""
Bucle while, break, continue
bucle infinito
"""

"""
# Bucle infinito
while True:
    pass
"""

# Validar un importe: sólo se aceptan múltiplos de 10
"""
importe = int(input("Teclear importe:"))
while importe % 10 != 0:
    print("El importe es incorrecto")
    importe = int(input("Teclear importe:"))
"""

while True:
    sImporte = input("Teclear importe:")
    if sImporte.isnumeric():
        importe = int(sImporte)
        if importe % 10 == 0:
            break
        else:
            print("El número no es múltiplo de 10")
    else:
        print("Solo se aceptan número enteros")

print("importe: ", importe)
