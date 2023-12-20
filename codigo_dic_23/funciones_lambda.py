"""
Programación funcional en Python
"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def invertir(s):
    return s[::-1]


def operar(operacion, *args):
    return operacion(*args)


print(operar(suma, 1, 2))
print(operar(resta, 10, 2))
s = "{}({},{})".format("suma",3,4)
print(s)
print(eval(s))
exit()

f = invertir
print(f, type(f))
print(f("hola"))
