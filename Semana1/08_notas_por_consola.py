"""
las notas no pueden ser ni mayores que 5 ni menores que  0
"""
notas_estudiante = []


cantidad_notas =int(input("Ingrese la cantidad de notas de juan :")) #3
i = 0
while i < cantidad_notas:
    nota = float(input(f"ingrese la nota {i+1}: "))
    if nota < 0 or nota >5:
        print("la nota no esta entre 0 y 5, intente denuevo")
    else:
        notas_estudiante.append(nota)
        i = i +1 # i += 1


print(f"calificaciones de juan {notas_estudiante}")