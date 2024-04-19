"""
Implementación de un servidor TCP
"""

import socket as s
import sys
from threading import Thread


class HiloCliente(Thread):

    def __init__(self, s_client, addr):
        Thread.__init__(self)
        self.s_client = s_client
        self.addr = addr

    def run(self):
        while True:
            # Recibir:
            mensaje = self.s_client.recv(1024)
            mensaje = mensaje.decode("utf-8")
            if mensaje.lower() == "fin":
                break

            print(mensaje)
            self.s_client.send(mensaje.upper().encode("utf-8"))

        print("Fin de comunicación")

    def __del__(self):
        if hasattr(self, "s_client"):
            self.s_client.close()


if len(sys.argv) == 2:
    puerto = int(sys.argv[1])
    print("Puerto: ", puerto)

    s_server = None
    try:

        # Crear un socket TCP / AF_INET
        s_server = s.socket()
        s_server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        print("Socket creado ...")

        # Bind:
        s_server.bind(("localhost", puerto))
        print("Bind ok!")

        # Comunicacion 1 a n:
        s_server.listen(10)

        while True:
            print("Servidor a la espera de clientes")
            s_client, addr = s_server.accept()
            print("cliente conectado: ", addr)

            cliente = HiloCliente(s_client, addr)
            cliente.start()

    except Exception as e:
        print("ERROR: ", e)

    except KeyboardInterrupt as e1:
        print("Servidor Control+C")

    finally:

        if s_server:
            s_server.close()

else:
    print("No se ha indicado el puerto para conectar ...")
