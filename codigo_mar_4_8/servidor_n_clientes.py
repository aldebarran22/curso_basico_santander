"""
Implementación de un servidor TCP
"""

import socket as s
import sys
from threading import Thread


class Cliente(Thread):

    def __init__(self, s_client, addr):
        self.addr = addr
        self.s_client = s_client

    def run(self):
        # Recibir:
        try:
            while True:
                mensaje = self.s_client.recv(1024)
                mensaje = mensaje.decode("utf-8")
                if mensaje.lower() == "fin":
                    break

                print("Mensaje del cliente: ", self.addr, "Mensaje:", mensaje)
                self.s_client.send(mensaje.upper().encode("utf-8"))
        except Exception as e:
            if e.errno == 10054:
                print("Cliente desconectado")
            else:
                print(e)


if len(sys.argv) == 2:
    puerto = int(sys.argv[1])
    print("Puerto: ", puerto)

    s_server = s_client = None
    try:
        # Crear un socket TCP / AF_INET
        s_server = s.socket()
        s_server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        print("Socket creado ...")

        # Bind:
        s_server.bind(("localhost", puerto))
        print("Bind ok!")

        # Comunicacion 1 a 1:
        s_server.listen(5)

        while True:
            print("Servidor a la espera de clientes")
            s_client, addr = s_server.accept()
            print("cliente conectado: ", addr)

            cliente = Cliente(addr, s_client)
            cliente.start()

        print("Fin de comunicación")

    except Exception as e:
        print("ERROR: ", e)

    except KeyboardInterrupt as e1:
        print("Servidor Control+C")

    finally:
        if s_client:
            s_client.close()
        if s_server:
            s_server.close()

else:
    print("No se ha indicado el puerto para conectar ...")
