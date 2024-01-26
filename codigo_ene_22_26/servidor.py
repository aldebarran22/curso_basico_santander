"""
Servidor TCP en Python
"""
import socket

s = socket.socket()
# Reutilizar el puerto
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket creado!")
s.bind(("localhost", 9999))
print("Bind ok!")
s.listen(1)
print("Servidor a la espera de clientes ...")
sc, addr = s.accept()
print("Cliente conectado: ", addr)
while True:
    recibido = sc.recv(1024)
    recibido = recibido.decode("utf-8")
    if recibido == "quit":
        break
    print("Recibido:", recibido)
    sc.send(recibido.encode("utf-8"))
print("fin comunicación")
sc.close()
s.close()
