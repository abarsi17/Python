# ========
# Asignación de una mesa
# ========

# Tipo de mesa
P2 = 2  # 2 plazas
P4 = 4  # 4 plazas
P6 = 6  # ...
P8 = 8

# Tipo de sala
SALA1 = 1
TERRAZA = 9

# Mesas con un diccionario simple con el nº como clave y
# las características número de plazas, sala en una tupla

MESAS = {
    1: (P2, TERRAZA),
    2: (P2, TERRAZA),
    3: (P4, TERRAZA),
    4: (P4, TERRAZA),
    5: (P6, TERRAZA),
    6: (P8, TERRAZA),

    11: (P2, SALA1),
    12: (P2, SALA1),
    13: (P4, SALA1),
    14: (P4, SALA1),
    15: (P6, SALA1),
    16: (P8, SALA1),
    }

# Encontrar una mesa para n personas

def encontrar_mesa(nPersonas):
    for clave,valor in MESAS.items():
        if nPersonas <= valor[0]:
            return clave

def mesa(nPersona):
    valor = encontrar_mesa(nPersona)

    if valor:
        print("Encontrada mesa Nº", valor, "en", end='')

        if MESAS[valor][1] == TERRAZA:
            print(" TERRAZA")
        elif MESAS[valor][1] == SALA1:
            print(" la SALA nº 1")

if __name__ == '__main__':
    mesa(2)

