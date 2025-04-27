"""Calculadora simple en Python"""

# entrada de datos
print("Bienvenido a la calculadora")
print("Seleccione una opcion:")
opciones_msg = """
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    
    """
menu = int(input(opciones_msg))
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if menu == 1:
    resultado = numero_1 + numero_2
    operacion = "+"
elif menu == 2:
    resultado = numero_1 - numero_2
    operacion = "-"
elif menu == 3:
    resultado = numero_1 * numero_2 
    operacion = "x"
elif menu == 4:
    if numero_2 == 0:
        print("No se puede dividir entre cero")
        resultado = None
    else:
        resultado = numero_1 / numero_2
        operacion = "/"
        
else:
    print("Opcion no valida")
    print("Por favor seleccione una opcion valida")

if resultado is not None:
    print("El resultado es:")
    print(f"El resultado de {numero_1}  {operacion} {numero_2} = {resultado}")
print("Fin del programa")