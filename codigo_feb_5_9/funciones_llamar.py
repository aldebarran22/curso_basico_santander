"""
Formas de llamar a una función en Python
1) Posicional
2) Nominal
3) Con una tupla / lista
4) Con un diccionario
"""


def sumar(a, b):
    return a + b


print(sumar(1, 3))  # Posicional
print(sumar(b=3, a=1))  # Nominal
t = (1, 3)
print(sumar(t[0], t[1]))  # incómodo!!!
print(sumar(*t))  # Con el * desempaqueta la tupla
d = {"a": 1, "b": 3}
print(sumar(**d))  # desempaqueta el dict.

########################################################################
# Ejemplo


def formatearHora(h=0, m=0, s=0):
    print("%02d:%02d:%02d" % (h, m, s))


horas = [(13, 45, 0), (8, 1, 34), (12, 30), (17,)]
# 13:45:00, 08:01:34, 12:30:00, 17:00:00
for i in horas:
    formatearHora(*i)

# Llamadas a un función con parámetros opcionales:
formatearHora(s=30)
formatearHora(m=10)

##################################################################

def calcularIVA(precio, iva=21.0):
    return round(precio * iva / 100, 2)

print('iva de 100: ', calcularIVA(100))
print('iva de 150 al 10%: ', calcularIVA(150, 10.0))
print('iva de 200 al 4%: ', calcularIVA(150, 4.0))
