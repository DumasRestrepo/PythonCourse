"""
Programa de validación de clave de acceso.

Este programa solicita al usuario una clave y permite hasta un máximo de intentos.
Si el usuario ingresa la clave correcta, se le concede acceso.
Si se agotan los intentos permitidos, se deniega el acceso.

- Máximo de intentos: 3
- Clave correcta: "python123"
"""

clave_correcta = "python123"
MAX_REINTENTOS = 3
intentos = 0
acceso_concedido = False

while intentos < MAX_REINTENTOS:
    clave = input("🔐 Ingrese su clave: ")

    if clave == clave_correcta:
        acceso_concedido = True
        break
    else:
        intentos += 1
        print(f"Clave incorrecta. Intentos restantes: {MAX_REINTENTOS - intentos}")

if acceso_concedido:
    print(" Acceso concedido. Bienvenido.")
else:
    print("Ha superado el número de intentos permitidos. Acceso denegado.")

print("Fin del programa.")
