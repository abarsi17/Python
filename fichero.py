#Abrir fichero
##ficheroRead = open('prueba.txt', 'r')
ficheroRead = open('prueba.txt')

#Leer fichero entero
##entero = ficheroRead.read()

#Leer líneas enteras
lineas = ficheroRead.readline()

#Leer todas las líneas
##lineas = ficheroRead.readlines()

#Leer carácter a carácter
##caracter = ficheroRead.readline(1)

ficheroWrite = open('pruebaWrite.txt', 'w')

for l in lineas:
    print("linea = %s" % l)

for char in lineas:
    if char == "a":
        ficheroWrite.write(char)

"""for l in ficheroRead:
    print("l = %s" % l, end='')
"""

ficheroWrite.close()

ficheroRead.close()