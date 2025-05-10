def is_adult(edad_de_la_persona:int):
        return edad_de_la_persona>=18 #True si es es mayor o False si es menor

def ingreso_datos()->int:
    try:
        numero = input("ingrese la edad de la persona ")
        return int(numero)
    except:
        print("Valor ingresado no valido")
        return None

if __name__ == '__main__':
    edad = None
    while edad == None:
        edad = ingreso_datos()

    if is_adult(edad):
        print("Adelante, usted es mayor de edad")
    else:
        print("Lo lamento, no puede ingresar")

    print("FIN DEL PROGRAMA")     

