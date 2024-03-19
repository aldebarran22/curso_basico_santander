"""
Validar datos de teclado. Sólo se aceptan
importes múltiplos de 10
"""

while True:
    sImporte = input("Teclear importe:>")
    if sImporte.isnumeric():
        importe = int(sImporte)
        if importe % 10 == 0:
            break
        else:
            print("El importe debe ser un múltiplo de 10.")
    else:
        print('Sólo se acpetan números')


