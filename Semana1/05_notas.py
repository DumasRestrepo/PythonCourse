"promedio de notas"

juan =[4.5, 3.5, 4.0, 2.5,4,5,2,0,1]
print(len(juan))
"""
nota =4,5
suma_notas = 0
suma_notas = 4,5

nota =3,5
suma_notas = 4,5 + 3,5
suma_notas = 8,0

nota =4,0
suma_notas = 8,0 + 4,0
suma_notas = 12,0
"""

#calcular el promedio  suma todo y divide entre la cantidad de notas
promedio = 0
suma_notas = 0
for nota in juan:
    suma_notas = suma_notas + nota

promedio = suma_notas / len(juan)

print(f"El promedio de notas es: {promedio}")

if promedio >= 3.0:
    print("El estudiante aprobo")
else:
    print("El estudiante reprobo")


