#          0    1    2
#notas = [3.5, 4.2, 5.0]
nota1 = 3,5
nota2= 4.2
estudiante_1 = {"nombre":"Alex",
              "edad":18,
              "is_adult": True,
              "calificaciones": [4.5, 4.2, 5.0]}

estudiante_2 = {"nombre":"Maria",
              "edad":17,
              "is_adult": False,
              "calificaciones": [3.5, 4.2, 5.0]}



list_estudiantes =[estudiante_1, estudiante_2]
print(list_estudiantes)

print("(*****)")
for estudiante in list_estudiantes:

    for llave,valor in estudiante.items():

        if llave == "calificaciones":
            print("la segunda calificaion es: ",valor[1])
            valor[1] = 5
    print(list_estudiantes)