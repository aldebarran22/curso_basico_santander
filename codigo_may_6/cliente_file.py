"""
Ejemplo de socket para un cliente
"""

import socket
import sys

HOST = "localhost"  # 127.0.0.1

if len(sys.argv) == 3:
    puerto = int(sys.argv[1])
    print("Puerto: ", puerto)
    path_fich = sys.argv[2]
    print("Path: ", path_fich)

    sock_c = None
    fich = None
    try:
        # Abrir el fichero en modo lectura
        fich = open(path_fich, "r")

        # Crea un socket para el cliente:
        sock_c = socket.socket()

        # Se conecta con el servidor:
        sock_c.connect((HOST, puerto))

        for linea in fich:
            linea = linea.rstrip()
            if len(linea) == 0:
                continue

            # Enviamos un mensaje al server:
            sock_c.send(linea.encode("utf-8"))

        # Indicar que hemos terminado:
        sock_c.send("fin".encode("utf-8"))

    except Exception as e:
        print("ERROR", e)

    except KeyboardInterrupt as e:
        print("Interrupcion de teclado")
        sock_c.send("fin".encode("utf-8"))

    finally:
        if sock_c != None:
            sock_c.close()
        if fich != None:
            fich.close()

else:
    print("python cliente_file.py <<puerto>> <<fichero>>")
