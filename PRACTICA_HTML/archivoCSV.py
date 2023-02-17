import documentPOO
import random

class CSV(documentPOO.Document):
    
    def __init__(self, titulo="Página HTML", autor="root"):
        super().__init__(titulo, autor)
        self.contenido = []
        self.separador = ';'
        self.fin_de_linea = '\n'

    def __str__(self):
        t = ""
        t += self.titulo + self.fin_de_linea
        ## Copia del atributo contenido en una copia temporal
        ## Se hace la copia, ya que la función pop destruye la lista
        tmp = list(self.contenido)

        ## Extracción de los encabezados
        for e in tmp.pop(0):
            t += "%s" % e
            t += self.separador
        t += self.fin_de_linea
    
        ## Los datos
        for l in tmp.pop():
            for d in l:
                t += "%s" % d
                t += self.separador
            t += self.fin_de_linea
        return t

    def __repr__(self):
        return "<CSV: %s : %d >" % (self.titulo, id(self))
    
if __name__ == "__main__":
    P = CSV()
    P.titulo = "RESULTADO DE LAS COPIAS DE SEGURIDAD"
    encabezado = ['FECHA', 'PROD', 'EVOLUTIVO', 'DEV & TEST']

    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    resultado = ['OK', 'Error', '']
    
    Data = []
    for n in range(0, 5):
        d = [dias[n], random.choice(resultado), random.choice(resultado), random.choice(resultado)]
        Data.append(d)
    P.contenido.append(encabezado)
    P.contenido.append(Data)

    print(P)