"""
Mostrar información en columnas
"""
# Abrir un fichero para grabar datos
fich = open("productos.txt", "w")
L = [("HP", 1245.967), ("Teclado", 45.5), ("Ratón", 15.0)]
for producto, precio in L:
    print("%-12s\t%8.2f" % (producto, precio), file=fich)
fich.close()
