# Menu de comida rapida
MENU = [
    ["Ensalada César", 15],
    ["Ensalada ilustrada", 14],
    ["Ensalada de pollo", 16],
    ["Ensalada verde", 10],
]

def menu():
    print("Nuestro menú: \n")
    for plato in MENU:
        desc = plato[0]
        precio = plato[1]
        print("%20s: %5.2f euros" % (desc, precio))

if __name__ == '__main__':
    menu()