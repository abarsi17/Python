import documentPOO
import random

# paginaHTML hereda de la clase padre Document
class paginaHTML(documentPOO.Document):
    def __init__(self, titulo='Pagina', autor = 'root'):
        super().__init__(titulo, autor)
        self.contenido = [] # Forzar para que sea una cadena vacía

    def head(self):
        return """
    <head>
        <title> %s </title>
    </head>
        """ % (self.titulo)
    
    def body(self):
        return """
    <body>
        %s
    </body>
        """ % (self.devuelve_contenido())

    def footer(self):
        return """
    <footer>
        %s
    </footer>
        """ % (self.fecha_creacion)

    def __str__(self):
        return """
<html>
%s
%s
%s
</html>
        """ % (self.head(), self.body(), self.footer())


    def add_table(self, encabezado, data):
        theader = ""
        for h in encabezado:
            theader += "<th>%s</th>" % h
        tbody = ""
        for l in data:
            tbody += "<tr>"
            for r in l:
                tbody += "<td>%s</td>" % r
        t = """
        <table border=1>
            <thead>
            <tr>%s</tr>
            </thead>
            <tbody>
            %s
            </tbody>
        </table>""" % (theader, tbody)
        self.contenido.append(t)
    
    def __repr__(self):
        return """<Documento HTML: %s : %d>""" % (self.autor, id(self))

if __name__ == '__main__':
    html = paginaHTML()
    html.titulo = "Pagina HTML"
    encabezado = ["Fecha", "PROD", "EVOLUTIVO", "DEV & TEST"]

    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    resultado = ['OK', 'Error', '&nbsp']
    
    Data = []
    for n in range(0, 5):
        d = [dias[n], random.choice(resultado), random.choice(resultado), random.choice(resultado)]
        Data.append(d)
    html.add_table(encabezado, Data)
    print(html)

