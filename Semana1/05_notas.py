"promedio de notas"

juan =[4.5, 3.5, 4.0, 2.5,4,5,2,0,1]

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


