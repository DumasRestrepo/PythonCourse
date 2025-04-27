"""condionales_menu.py
Comparar dos numeros enteros
"""

# Declaracion de variables
numero_1 = 0
numero_2 = 0
resultado = 0

# entrada de datos
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
# proceamiento y salida}
if numero_1 == numero_2:
    print(f"Los numeros son iguales {numero_1} == {numero_2}")
else:
    if numero_1 > numero_2:
        print(f"El numero mayor es {numero_1} y el menor es {numero_2}")
    else:
        print(f"El numero mayor es {numero_2} y el menor es {numero_1}")



