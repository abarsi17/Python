# Importar paquete que se almacena en la misma path

import modulo
import time
from countSort import countsortNum

modulo.mi_funcion()
for i in list(range(3)):
    print(i, "||")

lista = list(range(4))
it = iter(lista)

for i in it:
    print(i)

print(time.asctime())

vector = [10, 5, 9, 2, 3, 6, 6]
vector = countsortNum(vector)
for i in vector:
    print(i)
