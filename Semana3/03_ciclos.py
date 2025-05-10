# condicionales if elif else #for in range for each


"validar que el dato que se ingrese por tecladosea un numero"
numero = 0

while numero != '-1': # Si e el numero ingresado es -1 finializa el ciclo
    numero = input("ingrese un numero entero") # input por defecto guarda como Str
    numero_temporal = numero.replace('-','')
    if numero_temporal.isdigit(): # True si la cadena de texto es solo numeros # False si es texto
        print(f"Felicitaciones el numero {numero}, es un numero entero")
    else:
        print(f"Malas noticias lo que ingreso ({numero}), no es un numero entero")

