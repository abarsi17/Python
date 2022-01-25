import modulo
import time
modulo.mi_funcion()
for i in list(range(3)):
    print(i, "||")

lista = list(range(4))
it = iter(lista)

for i in it:
    print(i)

print(time.asctime())
