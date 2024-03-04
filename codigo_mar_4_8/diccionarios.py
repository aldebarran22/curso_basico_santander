"""
Diccionarios en Python:
{}, dict, zip
acceso a los elementos
crear nuevas claves
"""
d = {'a':1, 'b':2, 'c':3, 'd':4}
print(d['a'])
d['e'] = 5
print(d, type(d))

L = [1,2,3,4,5]
cad = "adios"
d2 = dict(zip(L, cad))
print(d2)
d3 = dict(zip(cad, L))
print(d3)

# in, for
d = {'a':1, 'b':2, 'c':3, 'd':4}
print('Existe la clave: c: ', 'c' in d)
print('Existe el valor: 2: ', 2 in d.values())

