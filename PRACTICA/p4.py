# Declaración de variable global
global lista

# Pasar listas a funciones
lista = [1, [1,2,3], "dos", 2.0]

def f1(*args):
    for iter, i in enumerate(args):
        print("Posición: ", iter, "\t|\tValor: ", i)

# La lista hay que pasarla poniendo el *, si no es como si la pasaramos como un único valor
f1(*lista)

# Variable por referencia (enviar una copia) [:] -> cuando se llama a la función f2(lista[:])
def f2(args):
    args.append("VALOR")
    return args

import random
import time

from PRUEBAS_MODULOS import *

def p():
    while True:
        valor = random.random()*100
        print(valor, int(valor), sep=" - ")
        time.sleep(1)

fichero.test()