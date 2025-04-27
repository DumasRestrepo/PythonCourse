"""
Muestre un mensaje indicando si deea ver los pares de 0 a 1000 o los impares de 0 a 1000
"""
msj = """
    1. Pares
    2. Impares
"""
opcion = int(input(msj))

if opcion == 1:
    for numero in range (0, 1001):
        if numero % 2 == 0:
            print(numero)
elif opcion == 2:
    for numero in range (1, 1001, 2):
        print(numero)

