"""
Crear histogramas con diccionarios
"""

paises = """99;Estados Unidos
32.38;Finlandia
11.61;Alemania
65.83;Brasil
41.34;Francia
51.3;Belgica
58.17;Brasil
22.98;Suiza
148.33;Suiza
13.97;Brasil
81.91;Venezuela
140.51;Austria
3.25;Mexico
55.09;Alemania
3.05;Brasil
48.29;Estados Unidos
146.06;Austria
3.67;Suecia
55.28;Francia
25.73;Finlandia
208.58;Alemania
66.29;Venezuela
4.56;Estados Unidos
136.54;Finlandia
4.54;Estados Unidos
98.03;Estados Unidos
76.07;Alemania
6.01;Francia
26.93;Italia
13.84;Mexico
125.77;Alemania
92.69;Suecia
25.83;Alemania
8.98;Suecia
2.94;Espanya
12.69;Espanya
84.81;Venezuela
76.56;Alemania
76.83;Alemania
229.24;Alemania
12.76;Brasil
7.45;Italia
22.77;Reino Unido
79.7;Brasil
6.4;Brasil"""


"""
EJEMPLO:
Lpaises = [[99, "Estados Unidos"], \
           [32.38, "Finlandia"], \
            [11.61, "Alemania"]]

# EL segundo pedido:
print(Lpaises[1])

# El país del tercer pedido:
print(Lpaises[2][1])
"""

Lpaises = paises.split("\n")

# Crear un diccionario vacío:
total_paises = dict()

# Crear un histograma para calcular el importe
# total por pais:
for pedido in Lpaises:
    Lpedido = pedido.split(";")
    importe = float(Lpedido[0])
    pais = Lpedido[1]

    if pais in total_paises:
        # El país ya existe en el diccionario: incrementar el importe
        total_paises[pais] += importe
    else:
        # Es la primera vez que encontramos el país. Se crea una nueva
        # clave con el país y el importe:
        total_paises[pais] = importe

for pais, importe in total_paises.items():
    print(pais, round(importe,2))


# A que países se han emitido pedidos:
print("Países: ", total_paises.keys())
print('Tenemos: ', len(total_paises.keys()),"paises")
print('Total importe: ', round(sum(total_paises.values()),2))
