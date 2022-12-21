# Para que modifique el final de línea de la función print
for i in [1,2,3]:
    if i != 3:
        print(i, end="-")
    else:
        print(i)

# Para que separe cada número por /, únicamente si lo ponemos de esta manera
print(1,2,3, sep="/")

for i in range(0,5):
    if i == 2:
        continue # Salta a la siguiente iteración sin importar el código que haya debajo
        # break # Sale directamente del bucle
    print(i)

import random

encontrado = True
intentos = 0
num_rand = random.randint(0,5)

# Función else en el bucle
while not encontrado:
    print("Un numero entre 0 y 5: ")
    valor = input()
    intentos += 1

    if int(valor) == num_rand:
        encontrado = True

else:
    print("Encontrado en %s intentos" % intentos)

# enumerate(lista) se utiliza como iterador
for contador, valor in enumerate(['a', 'b', "c", "d"]):
    print("Contador: %s, Valor: %s" % (contador, valor))

# Lista de Lista
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']
l3 = [100, 200, 300, 400]

lista_de_lista = [l1, l2, l3]

print("Num | v1 |  v2 |  v3 |  v4 |")
print("============================")

# Al utilizar %3s %valor -> pone primero 3 espacios (de caracter) y despues el valor
for num, (v1, v2, v3, v4) in enumerate(lista_de_lista):
    print("%2s | %3s | %3s | %3s | %3s |" %(num,v1,v2,v3,v4))

# Lista de compresión -> utilizar la función for en una única línea
# Mostrar cifras pares
[print(x) for x in range(0,12) if not (x % 2)]

# Mostrar cifras impares
[print(x) for x in range(0,12) if  (x % 2)]
