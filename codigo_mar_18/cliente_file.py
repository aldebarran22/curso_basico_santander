"""
Ejemplo de socket para un cliente
"""

import socket
import sys

HOST = "localhost"  # 127.0.0.1

if len(sys.argv) == 3:
    puerto = int(sys.argv[1])
    print("Puerto: ", puerto)

    path = sys.argv[2]
    print("Fichero a transferir: ", path)

    sock_c = None
    fich = None
    try:
        fich = open(path, "r")

        # Crea un socket para el cliente:
        sock_c = socket.socket()

        # Se conecta con el servidor:
        sock_c.connect((HOST, puerto))

        for linea in fich:
            linea = linea.rstrip()

            # Enviamos un mensaje al server:
            sock_c.send(linea.encode("utf-8"))

            # Esperar el mensaje del Servidor:
            mensajeSer = sock_c.recv(1024)
            mensajeSer = mensajeSer.decode("utf-8")
            # print("El Server dice: ", mensajeSer)

        # Cortar comunicación con el Servidor!
        sock_c.send("fin".encode("utf-8"))

    except Exception as e:
        print("ERROR", e)

    except KeyboardInterrupt as e:
        print("Interrupcion de teclado")
        sock_c.send("fin".encode("utf-8"))

    finally:
        if sock_c != None:
            sock_c.close()

        if fich:
            fich.close()

else:
    print("Sintaxis: python cliente_file.py <<puerto>> <<fichero>>")
