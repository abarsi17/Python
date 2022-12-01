# Menu de comida rapida
MENU = [
    ["Hamburguesa", 10],
    ["Hamburguesa con queso", 10],
    ["Patatas fritas", 3],
    ["Ketchup", 0],
]

def menu():
    print("Nuestro menú: \n")
    for plato in MENU:
        desc = plato[0]
        precio = plato[1]
        print("%20s: %5.2f euros" % (desc, precio))

if __name__ == '__main__':
    menu()