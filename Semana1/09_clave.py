"""Programa para validación de clave"""
# Inicializar variables
clave = ""
intentos = 0
clave_actual = "python123"
REINTENTOS_PERMITIDO = 3
# Solicitar la clave al usuariogg

while clave != clave_actual and intentos <= REINTENTOS_PERMITIDO:
    if intentos == REINTENTOS_PERMITIDO:
        print("Ha superado la cantidad de intentos. Cerrando el programa")
        break
    else:
        clave = input("Ingrese su clave: ")
        if clave != clave_actual:
            print(" La clave ingresada no es correcta, intente nuevamente ")
            intentos += 1
        elif clave == clave_actual:
            print(" La clave ingresada es correcta, puede continuar ")
print("Fin del programa")
