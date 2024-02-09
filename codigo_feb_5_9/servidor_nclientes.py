"""
Servidor TCP en Python
"""

import socket
from threading import Thread


class HiloCliente(Thread):

    def __init__(self, cliente, addr):
        Thread.__init__(self)
        self.cliente = cliente
        self.addr = addr

    def run(self):
        try:
            while True:
                recibido = self.cliente.recv(1024)
                recibido = recibido.decode("utf-8")
                if recibido == "quit":
                    break
                print("Recibido:", recibido)
                self.cliente.send(recibido.encode("utf-8"))
            print("fin comunicación")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        s = socket.socket()
        # Reutilizar el puerto
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Socket creado!")
        s.bind(("localhost", 9999))
        print("Bind ok!")
        s.listen(3)
        print("Servidor a la espera de clientes ...")
        while True:
            sc, addr = s.accept()
            print("Cliente conectado: ", addr)

            # Por cada cliente que se conecta se habilita un hilo:
            hiloCliente = HiloCliente(sc, addr)
            hiloCliente.start()

        s.close()
    except Exception as e:
        print(e)
