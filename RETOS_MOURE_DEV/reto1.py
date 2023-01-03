
"""
    # Escribe un programa que reciba un texto y transforme lenguaje natural a
    # "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    #  se caracteriza por sustituir caracteres alfanuméricos.
    # - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
    #   con el alfabeto y los números en "leet".
    #   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
    #
"""

def leet():
    vocabularyLeet = ("4", "|3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "|_", "/\/\\", "/\/", "0", "|*", "(_,)",
     "12", "5", "7", "(_)", "\/", "\/\/", "><", "\|/", "2")
    text = ""

    while text != "exit":
        newText = ""
        print("Introduce un texto (para salir introduzca 'exit'): ")
        text = input()
        for char in text:
            if char != " ":
                pos = ord(char)-97
                newText += vocabularyLeet[pos]
            else:
                newText += " "
        print(newText)
    


if __name__ == "__main__":
    leet()