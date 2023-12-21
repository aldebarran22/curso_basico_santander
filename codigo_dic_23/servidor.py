"""
Servidor de sockets.
"""
import socket

puerto = 8888

s = socket.socket()
print("Se ha creado el socket...")
s.bind("localhost", puerto)
print("bind configurado!")
s.listen(1)
print("Servidor ok, a la espera de clientes")
sc, addr = s.accept()
while True:
    # Espera un mensaje del cliente
    recibido = sc.recv(1024)
    recibido = recibido.decode("utf-8")
    if recibido == "quit":
        break
    print("Recibido:", recibido)
    sc.send(recibido.encode("utf-8"))

print("fin del servidor")
sc.close()
s.close()
