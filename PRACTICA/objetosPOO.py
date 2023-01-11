# Para comprobar que se ejecuta el script actual
# Si no se ejecuta este script directamente, no se puede utilizar nada
# Ni importando en otro script
if __name__ == '__main__':  
    # Creamos una clase vacio, sin ningún parametro
    class Vacia:
        # Sobrecargar la función __str__, heredada de object 
        def __str__(self):
            t = "creado actualmente"
            return t

    # Creamos el objeto y lo asignamos
    v = Vacia()
    v1 = Vacia()

    # Esto comprueba si apunta al mismo objeto, en este caso sería falso
    # ya que se crean dos objetos distintos
    print(v is v1)

    v2 = v1

    # En este caso sería verdadero, ya que v2 apunta hacia el objeto v1
    print(v1 is v2)

    # Creamos un nuevo parametro y le asignamos un valor para el objeto v
    v.contador = 2


    



