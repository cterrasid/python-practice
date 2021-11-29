def palindrome(word):
    word = word.replace(" ", "").lower()
    return word and word == word[::-1]


def run():
    word = input("Escribe una palabra: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")

# Entry point de Python:
if __name__ == '__main__':
    run()