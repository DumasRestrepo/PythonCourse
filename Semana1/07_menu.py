""" Menu basico de opciones
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
"""
menu = 0
while menu != 5:
    print("Bienvenido a la calculadora")
    print("Seleccione una opcion:")
    opciones_msg = """
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
        """
    menu = int(input(opciones_msg))
    if menu == 1:
        print("Suma")
    elif menu == 2:
        print("Resta")
    elif menu == 3:
        print("Multiplicacion")
    elif menu == 4:
        print("Division")
    elif menu== 5:    
        print("Salir")
    else:
        print("Error, ingrese una opcion valida")
        


            
