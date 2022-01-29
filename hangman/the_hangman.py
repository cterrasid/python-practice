from os import listxattr
from random import choice

"""
Utilizar comprehensions, manejo de archivos y todo lo aprendido.

Pistas
Funcion enumerate
Metodo get de los diccionarios
La sentencia:
    os.system("cls") -> Windows
    os.system("clear") -> Unix
    para limpiar la pantalla

Opcional
Sistema de puntos
Dibujar ahorcado con codigo ASCII en la consola
Mejorar la interfaz
"""

def normalize(word):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        word = word.replace(a, b).replace(a.upper(), b.upper())
    return word.lower()

# Obtener la lista de palabras.
def get_word():
    with open("hangman/data.txt", "r", encoding="utf-8") as f:
        words = [normalize(word.strip()) for word in f]
# Elegir aleatoriamente una palabra de la lista.
    return choice(words)


def match_word(word, masked_word):
# Mostrar la palabra al usuario, enmascarada.
    
# Le pido al usuario que introduzca una letra y la guardo en una variable.
    letter = input("Introduce una letra: ")
    masked_word = list(masked_word)
#     Acumulo la letra en una variable.
#     Verifico letra por letra la palabra original:
    for i in range(len(word)):
#         Si hay coincidencias, desenmascaro la letra en la(s) posicion(es) correspondiente(s).
        if word[i] == letter:
            masked_word[i] = letter
    return "".join(masked_word)
#         Si no hay coincidencias, pinto "No" que se irá acumulando.
#         Siempre, pido al usuario otra letra.
#         Cuando todas las letras esten desenmascaradas, pinto "Ganaste".
# Presionar <enter> para reiniciar el juego.

def run():
    word = get_word()
    masked_word = "*"*len(word)
    print(word)
    while masked_word != word:
        print(masked_word)
        masked_word = match_word(word, masked_word)
    else:
        print(masked_word)
        print("Ganaste!")


if __name__ == "__main__":
    run()