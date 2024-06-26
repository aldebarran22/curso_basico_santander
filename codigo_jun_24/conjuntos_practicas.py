txt2 = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""

txt3 = """id;nombre;cargo
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Gerente de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas
10;George;Representante de ventas"""


def ordenar(fila):
    aux = fila.partition(";")[0]
    if aux.isnumeric():
        return int(aux)
    else:
        return -1
    
def ordenarNombre(fila):
    nombre = fila.split(";")[1]
    if nombre == "nombre":
        return "0"
    else:
        return nombre
    

c2 = set(txt2.split("\n"))
c3 = set(txt3.split("\n"))
todo = c2 | c3
L = [fila for fila in todo if "nombre" not in fila]
R = sorted(L, key=ordenar)
R.insert(0, "id;nombre;cargo")
csv = "\n".join(R)
print(csv)
