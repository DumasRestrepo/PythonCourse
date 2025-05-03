def suma_dos_numeros(x,y): # x = 4 y y = 5
    r = x + y
    print(f'El resultado de la operacion es: {r}')


def restar_dos_numeros(x,y):
    resultado = x - y
    print(f'El resultado de la operacion es: {resultado}')

def dividir_de_forma_segura(x,y):
    if y != 0:
        resultado = x / y # Float
    else:
        resultado = "No es posible dividir entre 0 " # Str
    print("El resultado es: ", resultado) 


def mostrar_menu():
    print("CALCULADORA BASICA")
    print("""
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Salir
          """)
    
def ingreso_de_datos():
   while True:
    try:
        numero_1 = float(input("ingrse el primer numero:  "))
        numero_2 = float(input("Ingrese el segundo numero:  "))
    except:
        print("A ingresado un valor no soportado")
    else:
        return numero_1, numero_2 # esto se ejecuta solo si el codigo no tiene excptiones


if __name__ == '__main__':
    mostrar_menu()
    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        a,b = ingreso_de_datos()
        suma_dos_numeros(a, b)
    elif opcion == 2:
        a,b = ingreso_de_datos()
        restar_dos_numeros(a, b)
    elif opcion == 3:
        pass
    elif opcion ==4:
        a,b = ingreso_de_datos()
        dividir_de_forma_segura(a,b)
    elif opcion == 5:
        pass
    else:
        print("Ingrese una opcion valida")
    
    
