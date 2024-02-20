"""
Contar el número de repetidos de una lista
creando un histograma: list, dict, set
"""
L = [1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 3, 2, 1, 2]
d = dict()
for i in L:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)