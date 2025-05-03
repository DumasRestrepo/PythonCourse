def suma_dos_numeros(x,y): # x = 4 y y = 5
    r = x + y
    print(f'El resultado de la operacion es: {r}')


def restar_dos_numeros(x,y):
    resultado = x - y
    return resultado

if __name__ == '__main__':
    print("CALCULADORA")
    numero_1 = int(input("Ingrese el numero 1: ")) # 4
    numero_2 = int(input("Ingrese el numero 2: "))# 5
    suma_dos_numeros(numero_1, numero_2) # suma_dos_numeros(4 , 5)

    resultado_resta = restar_dos_numeros(numero_1,numero_2)
    print(f"El resultado de la resta es: {resultado_resta}" )

    print("*******")
    print("El resultado de la resta opcion2 es ",restar_dos_numeros(numero_1,numero_2))
    
