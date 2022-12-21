# Lectura de un archivo del sistema

archivo = '/etc/passwd'

##a = open(archivo)

"""cont = 0
for l in a.readlines():
    if l.split(':')[0] == "root":
        print("Linea[%d]: %s" %(cont, l))
    cont += 1"""

with open(archivo) as f:
    for index, l in enumerate(f):
        # Ya que el archivo al principio contiene comentarios
        if l[0] != '#':
            user, pswd, id_u, id_g, com, home, shell = l.split(':')
            print("User = %s" % user)
            print("UID = %s" % id_u)
            print("GID = %s" % id_g)
            print("COMMENT = %s" % com)
            print("Home = %s" % home)
            print("Shell = %s" % shell)