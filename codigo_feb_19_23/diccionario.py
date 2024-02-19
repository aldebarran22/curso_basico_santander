"""
Diccionarios en Python
"""

d = {'a':1, 'b':2, 'c':3, 'd':4}

# Acceso a los elementos:
print(d['a'])
# print(d['x']) Error si la clave no existe

d['e'] = 5
d['d'] = 400
print(d, type(d))

# in
if 'e' in d:
    print('la clave e existe')
if 400 in d.values():
    print('400 existe')

print('claves: ', list(d.keys()))
print('valores: ', list(d.values()))
print('items: ', list(d.items()))
for k,v in d.items():
    print(k,v)