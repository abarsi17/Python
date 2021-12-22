
#FUNCIONES
def mi_funcion (param1):
    print param1

"""se utiliza *otros, para pasarle un valor o mas de un valor"""
def funcion (*otros):
    for elemento in otros:
        print elemento

funcion(1,2,3)

def varios(param1, param2, **otros):
       for i in otros.items():
           print i
varios(1, 2, tercero = 3)

def f(x, y): 
    x=x+ 3
    y.append(23)
    print (x, y)

x = 22
y = [22]
f(x, y)
print (x, y)

class Coche:
    """Abstraccion de los objetos coche."""
    #CONSTRUCTOR __init__
    def __init__(self, gasolina):
        self.gasolina = gasolina
        self.ruedas = 4
        self.marca = "Ferrari"
        print ("Tenemos", gasolina, "litros")
    def arrancar(self):
        if self.gasolina > 0:
            print ("Arranca")
        else:
            print ("No arranca")
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print ("Quedan", self.gasolina, "litros")
        else:
            print ("no se mueve")
    def getMarca (self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca
        

mi_coche = Coche(3)
mi_coche.arrancar()
print (mi_coche.getMarca())
mi_coche.setMarca("Porsche")
print (mi_coche.getMarca())



