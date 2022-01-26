import random


def run():
    random_number = random.randint(1, 100)
    user_number = int(input("Elige un número del 1 al 100: "))
    while random_number != user_number:
        if user_number > random_number:
            print("Elige un número más pequeño")
        else:
            print("Elige un número más grande")
        
        user_number = int(input("Elige otro número: "))
    else:
        print("¡Ganaste!")


if __name__ == "__main__":
    run()