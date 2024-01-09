"""
Ejemplo de funciones en Python
"""

def sumar(a,b):
    return a+b

def sumar3(a,b,c):
    return a+b+c

def imprimirPosiciones(t, numero):
    ini = 0
    for i in range(t.count(numero)):
        pos = t.index(numero, ini)
        print(pos)
        ini = pos + 1

print(sumar(3,5))
s = sumar(3,5)
print(s)
print(sumar("55","44"))

imprimirPosiciones((1,2,3,4,5), 5)



