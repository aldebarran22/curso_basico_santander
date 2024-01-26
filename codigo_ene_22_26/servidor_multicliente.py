"""
Servidor TCP en Python
"""
import socket
from threading import Thread


class HiloServer(Thread):
    def __init__(self, sc, addr):
        Thread.__init__(self)
        self.sc = sc
        self.addr = addr

    def run(self):
        while True:
            recibido = self.sc.recv(1024)
            recibido = recibido.decode("utf-8")
            # if recibido == "quit":
            #    break
            print("Recibido:", recibido)
            self.sc.send(recibido.encode("utf-8"))

        print("fin comunicación")
        self.sc.close()


if __name__ == "__main__":
    s = socket.socket()
    # Reutilizar el puerto
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket creado!")
    s.bind(("localhost", 9999))
    print("Bind ok!")
    s.listen(5)
    while True:
        print("Servidor a la espera de clientes ...")
        sc, addr = s.accept()
        print("Cliente conectado: ", addr)

        # Crear un hilo para comunicarnos con el cliente:
        hilo = HiloServer(sc, addr)
        hilo.start()

    s.close()
