"""
Simular un cajero:
- Pedir un importe y tiene que ser múltiplo de 10
- Desglosar el importe en billetes de 50, 20 y 10
"""

sImporte = input("Dame importe:> ")
if sImporte.isnumeric():
    importe = int(sImporte)
else:
    print('Solo se admiten importes enteros')


