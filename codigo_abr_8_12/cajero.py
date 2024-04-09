"""
Simular un cajero:
- Pedir un importe y tiene que ser múltiplo de 10
- Desglosar el importe en billetes de 50, 20 y 10
- importe: 230 -> 4 de 50, 1 de 20, 1 de 10.
- importe: 200 -> 4 de 50
"""

while True:
    sImporte = input("Dame importe:> ")
    if sImporte.isnumeric():
        importe = int(sImporte)
        # Comprobar si es múltiplo de 10
        if importe % 10 == 0:
            break
        else:
            print("Solo se admiten múltiplos de 10")
    else:
        print("Solo se admiten importes enteros")

print("El importe a retirar es: ", importe)
desglose = dict()
billetes = [50, 20, 10]


"""
Bucle infinito
while True:
    pass
"""
