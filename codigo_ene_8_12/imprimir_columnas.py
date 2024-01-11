"""
Mostrar información en columnas
"""

L = [('HP',1245.967), ('Teclado',45.5),('Ratón',15.0)]
for producto, precio in L:
    print("%-12s\t%8.2f" % (producto, precio))
