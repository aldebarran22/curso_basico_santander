"""
Operadores relacionales y lógicos
"""

# Comprobar si una variable está dentro de un intervalo
edad_ini = 18
edad_fin = 65
edad = 4

if edad >= edad_ini and edad <= edad_fin:
    print('edad dentro del intervalo')
else:
    print('no lo cumple')

if edad_ini <= edad <= edad_fin:
    print('edad dentro del intervalo')
else:
    print('no lo cumple')

if not (edad_ini <= edad <= edad_fin):
    print('no lo cumple')
else:
    print('edad dentro del intervalo')

if edad < edad_ini or edad > edad_fin:
    print('no lo cumple')
else:
    print('edad dentro del intervalo')



