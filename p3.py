# Para que modifique el final de línea de la función print
for i in [1,2,3]:
    if i != 3:
        print(i, end="-")
    else:
        print(i)

# Para que separe cada número por /, únicamente si lo ponemos de esta manera
print(1,2,3, sep="/")
