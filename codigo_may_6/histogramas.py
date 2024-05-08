"""
Crear histogramas en Python:
Lista: almacenar todos los valores con repetidos
Diccionario: Llevar un recuento del número de repeticiones de cada valor
Conjunto: obtener las claves para el diccionario.
"""

L = [1, 2, 3, 4, 4, 3, 1, 1, 1, 5, 6, 7, 8, 9, 0, 8, 6, 4, 32, 1, 1, 2]
c = set(L)
# print(c)
histo = dict()
for i in c:
    histo[i] = L.count(i)

# histogramas
R = sorted(histo.items(), key=lambda t: t[1], reverse=True)
for numero, cuenta in R:
    print(f"{numero} se repite {cuenta} veces")


# Recorrer diccionario, acceder a un campo
