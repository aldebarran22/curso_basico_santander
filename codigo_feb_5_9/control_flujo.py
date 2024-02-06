"""
Bucles y condiciones:
for -> conocemos el número de iteraciones
while -> depende de una resp del user
if compacto
"""

# Bucle infinito en Python
#while True:
#    pass
    

# Opción 1:
while True:
    numero = int(input('Dame un multiplo de 10:'))
    if numero % 10 != 0:
        print('Sólo múltiplos de 10')
    else:
        print('ok, múltiplo de 10: ', numero)
        break # Rompe el bucle

# Opción 2:
numero = int(input('Dame un multiplo de 10:'))
print('opcion 2:')
while numero % 10 != 0:
    print('Sólo múltiplos de 10')
    numero = int(input('Dame un multiplo de 10:'))
print('ok, múltiplo de 10: ', numero)

