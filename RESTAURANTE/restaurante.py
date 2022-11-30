# Para que esto funcione, hay que crear el archivo __init__.py y añadir los modulos del package libresta
from libresta import *

num_pers = cliente.llegada_cliente()
print("Llegada de ", num_pers, " clientes")
print(bienvenido.hello())
