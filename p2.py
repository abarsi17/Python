#HERENCIA
class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    def tocar(self):
        print ('Estamos tocando musica')
    def romper(self):
        print ("Eso lo pagas tu")
        print ("Son") , self.precio, ("euros")
#para que un clase herede de otra hay que poner entre parentesis de la clase que hereda
class Bateria(Instrumento):
    pass
class Guitarra(Instrumento):
    #Instrumento.__init__(self, precio)
    #para modificar el constructor volveriamos a crear el metodo init
    def __init__(self, precio, cuerda):
        self.precio = precio
        self.cuerda = cuerda
    pass

instrumento = Instrumento(100)
instrumento.tocar()
guit = Guitarra(2, True)
print guit.cuerda

#HERENCIA MULTIPLE
"""un objeto puede heredar de mas de una clase"""
class Terrestre:
    def desplazar(self):
        print "El animal anda"

class Acuatico:
    def nadar(self):
        print "El animal nada"

#en este caso como hereda de dos clases, le pasamos ambas
class Cocodrilo(Terrestre, Acuatico):
    pass

cocodrilo = Cocodrilo()
cocodrilo.desplazar()
cocodrilo.nadar()