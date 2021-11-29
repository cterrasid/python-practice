def currency_converter(dollar_value, currency_name):
    currency_value = float(input("Introduce la cantidad de " + currency_name + ": "))
    dollar_converted = str(round((currency_value / dollar_value), 2))
    print("Tienes $"+dollar_converted+" dólares")
    
menu = """
Bienvenido al conversor de monedas.

Elige una opción:
[1] Euros
[2] Bolívares
[3] Kwanzas
"""

option = int(input(menu))

if option == 1:
    currency_converter(0.89, "Euro")
elif option == 2:
    currency_converter(0.22, "Bolívares")
elif option == 3:
    currency_converter(585, "Kwanzas")
else:
    print("Ingresa una opción válida, por favor.")
