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

L = [1,2,3,1,1,2,3,4,5,6,3,2,1,2]
d = dict()
for i in L:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
print(d)
"""
1:4
2:4
3:3
"""

# Crear un diccionario  a partir de dos colecciones:
cad = "adios"
L = [1,2,3,4,5]

d1 = dict(zip(cad, L))
print(d1)

d2 = dict(zip(L, cad))
print(d2)

cad = "ana"
L = [1,2,3]
d3 = dict(zip(cad, L))
print(d3)

