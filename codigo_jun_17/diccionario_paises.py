"""
Crear histogramas con diccionarios
"""

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

def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        return txt

    except Exception as e:
        raise e

    finally:
        if fich: fich.close()


try:
    paises = leerFichero("../ficheros_curso/paises.csv")
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

    L = sorted(total_paises.items(), key=lambda t:t[1], reverse=True)

    for pais, importe in L:
        print(pais, round(importe,2))


    # A que países se han emitido pedidos:
    print("Países: ", total_paises.keys())
    print('Tenemos: ', len(total_paises.keys()),"paises")
    print('Total importe: ', round(sum(total_paises.values()),2))

    print(total_paises.items())
    
except Exception as e:
    print(e)