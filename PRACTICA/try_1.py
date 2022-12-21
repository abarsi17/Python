# Funcionamiento del try ... catch

# Si el valor introducido es número realizará las instrucciones del else y del finally
# En cambio si el valor introducido es diferente a un número realizara el except y el finally

OK = False

while not OK:
    try:
        n = int(input("Escriba un número:"))
    except (TypeError, ValueError):
        print("Error de tipo...")
    else:
        print("Clausula else")
    finally: 
        print("Clausula finally")