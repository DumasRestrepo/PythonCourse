"""ejemplo"""

# Diagnóstico de anemia

# Solicitar edad y nivel de hemoglobina
edad = float(input("Ingrese la edad en meses o años (use decimal para meses, ex: 0.5 para 6 meses): "))
hemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

# Determinar el rango normal según la edad
if 0 <= edad <= 1/12:  # 0 a 1 mes (en años: 1 mes = 1/12 año)
    rango_normal_min = 13
    rango_normal_max = 26
elif 1/12 < edad <= 6/12:  # >1 mes y ≤6 meses
    rango_normal_min = 10
    rango_normal_max = 18
elif 6/12 < edad <= 12/12:  # >6 meses y ≤12 meses
    rango_normal_min = 11
    rango_normal_max = 15
elif 1 < edad <= 5:  # >1 año y ≤5 años
    rango_normal_min = 11.5
    rango_normal_max = 15
elif 5 < edad <= 10:  # >5 años y ≤10 años
    rango_normal_min = 12.6
    rango_normal_max = 15.5
elif 10 < edad <= 15:  # >10 años y ≤15 años
    rango_normal_min = 13
    rango_normal_max = 15.5
else:
    print("Edad fuera del rango establecido para la evaluación.")
    exit()

# Evaluar si la persona tiene anemia
if hemoglobina < rango_normal_min:
    print("Resultado: positivo (anemia)")
else:
    print("Resultado: negativo")
