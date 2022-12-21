# Convertir un archivo que le pasemos a hexadecimal

import os
import sys
import string

BUFFER = 32

def uso():
    u = """uso: %s nombre_de_archivo"""
    print(u % sys.argv[0])

def hdump(archivo):
    EOF = False
    nol = 0
    f = open(archivo, 'rb')
    while not EOF:
        record = f.read(BUFFER)
        if len(record) != BUFFER:
            EOF = True
        nol += 1
        print("%08d: " % nol, end='')
        var = 0
        for c in record:
            print("%02x" % c, end='')
            var += 1
            if var == 2:
                print(' ', end='')
                var = 0
        if EOF:
            for n in range(0, BUFFER - len(record)):
                print('  ', end='')
        print('  ', end='')
        for c in record:
            if chr(c) in string.whitespace:
                print(' ', end='')
            elif chr(c) in string.printable:
                print(chr(c), end='')
            else:
                print('.', end='')
        print()
    f.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        if os.path.exists(archivo):
            hdump(archivo)
        else:
            print("Archivo inexistente: %s" % archivo)
            uso()
    else:
        print("nombre del archivo: argumento obligatorio")
        uso()
