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
importe = int(input("Teclear importe:"))
while importe % 10 != 0:
    print("El importe es incorrecto")
    importe = int(input("Teclear importe:"))