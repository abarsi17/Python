import PRACTICA.documentPOO

# paginaHTML hereda de la clase padre Document
class paginaHTML(PRACTICA.documentPOO.Document):
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
    
    def __repr__(self):
        return """<Documento HTML: %s : %d>""" % (self.autor, id(self))

if __name__ == '__main__':
    html = paginaHTML()
    html.titulo = "Pagina HTML"
    html.contenido.append('<p> HOLA MUNDO! </p>')

    print(html)
