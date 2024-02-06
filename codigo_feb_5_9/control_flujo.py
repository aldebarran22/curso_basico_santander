"""
Bucles y condiciones:
for -> conocemos el número de iteraciones
while -> depende de una resp del user
if compacto
"""

# Bucle infinito en Python
#while True:
#    pass
    

while True:
    numero = int(input('Dame un multiplo de 10:'))
    if numero % 10 != 0:
        print('Sólo múltiplos de 10')
    else:
        print('ok, múltiplo de 10: ', numero)
