# CICLO WHILE
# Potencia de un número
def exponentiation(limit, number):
    counter = 0
    exponentiation = number**counter
    while exponentiation < limit:
        print(str(number)+" elevado a "+str(counter)+" es igual a: " + str(exponentiation))
        counter = counter + 1
        exponentiation = 2**counter

# Números hasta el límite
def counter(limit):
    count = 0
    while count < limit:
        count += 1
        print(count)

## CICLO FOR
# Números hasta cierto límite
for count in range(21):
    print(count)

if __name__ == "__main__":
    # exponentiation(100, 2)
    counter(10)