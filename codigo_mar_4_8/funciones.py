"""
Funciones en Python
- Llamar a una función
"""


def sumar(a, b):
    """Suma los dos parámetros que recibe"""
    return a + b


def calcularIVA(importe, tasa=2, iva=21):
    return round((importe + tasa) * iva / 100, 2)


def coordenadas(lat, lon):
    # Desempaquetar/expandir tuplas
    dirLat = "N" if lat > 0 else "S"
    dirLon = "E" if lon > 0 else "W"
    print(f"{abs(lat)}{dirLat}, {abs(lon)}{dirLon}")


# Formas de llamar a la función
# 1) forma posicional:
print(sumar(12, 34))
print(calcularIVA(100, 5, 10))

# 2) forma nominal:
print(sumar(b=34, a=12))
print(calcularIVA(100, iva=21))

# 3) Con una tupla: 
L = [(40.4, -3.68), (34, -77), (45.6, -12), (-45, 77)]
for t in L:
    coordenadas(*t)

# 4) Con un diccionario:
d = {"lat":40.4, "lon": -3.68}
coordenadas(d['lat'], d['lon'])
coordenadas(**d)
