def ingresar_datos_estudiante():
    pass # TODO Agregar la logica correspondiente aca 

def add_estudiantes(lista_estudiantes: list)->list:
    """
    Funcion para agregar un estudiante en formato diccionario a la lista de estudiantes
    Args: None
    Return
         lista_estudiantes (lista)
    """
    # Todo agregar logica para modficiar datos de estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    calificaciones = [] # float
    for nota in range(3):
        calificacion = float(input(f"Ingrese la calificacion {nota+1}:"))
        calificaciones.append(calificacion)
    estudiante ={
        "nombre":nombre,
        "aprobo": None,
        "calificaciones":calificaciones
        }
    estudiantes.append(estudiante)
    return estudiantes
    
def infore_aprobacion(lista_estudiantes):
    print("\nInforme De aprobacion")
    
    for estudiante in lista_estudiantes:
        estudiante = is_approved(estudiante) # TODO mover a la funcion de  add_estudiantes
        msj_temp = ""
        if estudiante['aprobo'] == True:
            msj_temp = "Aprobo"
        elif estudiante['aprobo'] == False:
            msj_temp = "No Aprobo"
        print(f"{estudiante['nombre']} -> {msj_temp}")
    print("Fin de informe \n")
    return estudiantes

def calcular_promedio(calificaciones): # lista de calificaiones
    suma_calificaciones = sum(calificaciones)
    cantidad_notas = len(calificaciones)
    promedio = suma_calificaciones / cantidad_notas
    return promedio

def is_approved(estudiante): # Recibe diccionario
    promedio = calcular_promedio(estudiante['calificaciones'])
    if promedio > 3:
        estudiante["aprobo"] = True
    else:
        estudiante["aprobo"] = False
        
    return estudiante

def menu():
    print("1. añadir estudiante")
    print("2. mostrar informe")
    print("3. Salir")

if __name__ == '__main__':
    estudiantes = []
    while  True:
        menu()
        opcion =int(input("Ingrese la opcion del menu que requiere: "))
        if opcion == 1:
            estudiantes = add_estudiantes(estudiantes)
            print(estudiantes)
        elif opcion == 2:
            estudiantes =infore_aprobacion(estudiantes)
        elif opcion == 3:
            break
        else:
            print("🚩🚩ingrese una opcion valida🚩🚩") 
    print("*** FIN DEL PROGRAMA ***")

    # TODO añadir funcionalidad para configurar cuantas notas se asignaran
    # TODO Añadir funcionalidad para modificar calificaiones existentes
    # TODO Añadir funcionalidad para Mostrar lista  de calificaciones del curso completo
    # TODO Añadir sub menu en informe para mostrar solo la lista de estudiantes que approbaron o no
    # TODO Añadir Diagrama de flujo de aplicativo completo

    lista_nombres = []
