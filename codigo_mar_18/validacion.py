"""
Validar datos de teclado. Sólo se aceptan
importes múltiplos de 10
"""

importe = int(input("Teclear importe:>"))
if importe % 10 == 0:
    print("es multiplo de 10")
else:
    print("no lo es")
