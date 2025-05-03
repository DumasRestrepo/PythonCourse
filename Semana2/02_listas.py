def calcular_promedio(lista_calificaciones:list)-> int: 
    """
    Esta funcion calcula el promedio de calificaciones dentro de una lista de flotantes o enteros
    Args:
        lista_calificaciones (list): Lista de las calificaciones del estudiante durante el modulo
    Return:
         promedio (int): El promedio de las calificaciones
    """
    # [3.9, 4.0 , 4,5]
    # sumatoria de cada calificacion / cantidad de notas
    suma_calificaciones = sum(lista_calificaciones)
    cantidad_notas = len(lista_calificaciones)
    promedio = suma_calificaciones / cantidad_notas
    return promedio

if __name__ == '__main__':
    print("ingrese las 3 calificaciones de Carlos")
    notas = []
    for nota in range(1,4):
        calificaion = float(input(f"ingrese la nota N {nota}: "))
        notas.append(calificaion)
    print(f'las notas del estudiante son : {notas}')
    promedio_carlos = calcular_promedio()
    print(f'El promedio de Carlos es: {round(promedio_carlos, 2)}')
    
        
