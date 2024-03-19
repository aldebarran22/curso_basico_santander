"""
Validar datos de teclado. Sólo se aceptan
importes múltiplos de 10
"""

while True:
    importe = int(input("Teclear importe:>"))
    if importe % 10 == 0:
        break
    else:
        print("El importe debe ser un múltiplo de 10.")


