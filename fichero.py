#Abrir fichero
ficheroRead = open('texto.txt', 'r')
#Leer fichero entero
##entero = ficheroRead.read()

#Leer líneas enteras
lineas = ficheroRead.readline()

#Leer carácter a carácter
#caracter = ficheroRead.readline(1)

ficheroWrite = open('prueba.txt', 'w')

for char in lineas:
    if char == "a":
        ficheroWrite.write(char)

ficheroWrite.close()
fichero.close()
