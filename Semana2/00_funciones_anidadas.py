"""Funciones anidadas"""

# funcion 1.2
def adios(nombre):
    print(f'hasta pronto {nombre}')

#Funcion 1
def run():
    print("HOLA! este es unprograma con fuciones")
    nombre = saludar() #funcion 1.1
    adios(nombre) # fucnion 1.2

# funcion 1.1
def saludar():
    nombre = input("¿Como te llamas? ")
    print(f'Hola! {nombre}, es un placer conocerte')
    return nombre

# Funcion principal (main -> punto de entrada)FUNCION  0 
if __name__ == '__main__':
    run() # funcion 1
    print("FIN DEL PROGRAMA")