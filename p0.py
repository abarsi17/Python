# para ejecutar el programa -> python p0.py
c = "Hola mundo"
edad = 18
boolT = True
boolF = False

# mostrar por pantalla el valor de la variable c
print(c)
print(edad, boolF)
print('hola %s' %edad)
print("holA", edad)
print(f'Hola {edad}')



""" comentar un 
    un paragrafo """

# LISTAS
l = ['paco', True, 23, [2, 3]] 
# TUPLAS, son estaticas, no se pueden modificar
t = (1, 2, 3) 
# DICCIONARIOS
d = {"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amelie": "Jean-Pierre Jeunet"}
# mostrar por pantalla el dicionario
print (d["Love Actually"])
#crear un array vació
vacio = []
#crear un array con diez 0's
vacio = [0 for i in range(10)]

# BUCLES FOR
""" sumarle uno a cada elemento de la lista
    range(4) crea una lista con 4 valores {0, 1, 2, 3}
"""
lista = list(range(4))
for elemento in range(4):
    lista[elemento] = elemento

for elemento in lista:
    print (elemento)


secuencia = ["uno", "dos", "tres"]
for elemento in secuencia:
    print (elemento)

# CONDICIONALES
if edad == 23:
    print ("igual")
elif edad < 22:
    print ("menor")
else:
    print ("mayor")

# OPERADORES
"""hace referencia a que && es equivalente a "and" o a "&"""

"""
    && = and, &
    || = or, |
    !  = not, ~
"""

if edad > 17 & edad < 20: # edad > 17 and edad < 20:
    print ("Correcto")
else:
    print ("incorrecto")

#  BUCLES WHILE
"""para que lea el numero, porque estamos mezclando strings con numeros"""
while edad < 20:
    edad = edad + 1
    print ("Felicidades " + str(edad))

#  para introducir valores por consola
print ("Para salir, introduzca: adios")
while True:
    entrada = input("> ")
    if entrada == "adios":
        break 
    else:
        print (entrada)

