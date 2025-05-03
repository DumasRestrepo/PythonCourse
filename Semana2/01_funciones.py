"""
calculadora_basica.py  Suma, resta, multiplicación y división segura
"""


def suma_dos_numeros(x: float, y: float) -> None:
    """Suma x + y y muestra el resultado por pantalla."""
    resultado = x + y
    print(f"El resultado de la operación es: {resultado}")


def restar_dos_numeros(x: float, y: float) -> None:
    """Resta x - y y muestra el resultado por pantalla."""
    resultado = x - y
    print(f"El resultado de la operación es: {resultado}")


def multiplicar_dos_numeros(x: float, y: float) -> None:
    """Multiplica x * y y muestra el resultado por pantalla."""
    resultado = x * y
    print(f"El resultado de la operación es: {resultado}")


def dividir_de_forma_segura(x: float, y: float) -> None:
    """Divide x / y validando la división por cero."""
    if y != 0:
        resultado = x / y  # float
    else:
        resultado = "No es posible dividir entre 0"  # str
    print(f"El resultado de la operación es: {resultado}")



def mostrar_menu() -> None:
    """Imprime el menú principal."""
    print(
        "\nCALCULADORA BÁSICA\n"
        "  1. Sumar\n"
        "  2. Restar\n"
        "  3. Multiplicar\n"
        "  4. Dividir\n"
        "  5. Salir\n"
    )


def ingreso_de_datos() -> tuple[float, float]:
    """Solicita dos números al usuario y los devuelve como float."""
    while True:
        try:
            numero_1 = float(input("Ingrese el primer número: "))
            numero_2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("⚠️  Ha ingresado un valor no soportado. Intente de nuevo.")
        else:
            return numero_1, numero_2  # solo se ejecuta si no hubo excepción

if __name__ == "__main__":
    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            a, b = ingreso_de_datos()
            suma_dos_numeros(a, b)
        elif opcion == 2:
            a, b = ingreso_de_datos()
            restar_dos_numeros(a, b)
        elif opcion == 3:
            a, b = ingreso_de_datos()
            multiplicar_dos_numeros(a, b)
        elif opcion == 4:
            a, b = ingreso_de_datos()
            dividir_de_forma_segura(a, b)
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Ingrese una opción válida.")
