
"""
    Escribe un programa que muestre por consola (con un print) los
    # números de 1 a 100 (ambos incluidos y con un salto de línea entre
    # cada impresión), sustiuyendo los siguientes:
    # - Múltiplos de 3 por la palabra "fizz"
    # - Múltiplos de 5 por la palabra "buzz"
    # - Múltiplos de 3 y de 5 por la palabra "fizzbuzz"
"""

def fizzbuzz():
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            print('fizzbuzz')
        elif n % 3 == 0:
            print('fizz')
        elif n % 5 == 0:
            print('buzz')
        else:
            print(n)

if __name__ == "__main__":
    fizzbuzz()