import socket
import sys
from datetime import datetime

serverRemoto = input("Ingrese el host a scannear: ")
IPserverRemoto = socket.gethostbyname(serverRemoto)

for port in range(1,1025):
    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resultado = sockt.connect_ex((serverRemoto, port))
    print(f"revisando el puerto {port}")
    if resultado == 0:
       print(f"Puerto {port} se encuentra abierto")
