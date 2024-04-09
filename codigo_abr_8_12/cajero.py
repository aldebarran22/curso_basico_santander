"""
Simular un cajero:
- Pedir un importe y tiene que ser múltiplo de 10
- Desglosar el importe en billetes de 50, 20 y 10
- importe: 230 -> 4 de 50, 1 de 20, 1 de 10.
"""

sImporte = input("Dame importe:> ")
if sImporte.isnumeric():
    importe = int(sImporte)
    # Comprobar si es múltiplo de 10
    # if
else:
    print("Solo se admiten importes enteros")

"""
Bucle infinito
while True:
    pass
"""
