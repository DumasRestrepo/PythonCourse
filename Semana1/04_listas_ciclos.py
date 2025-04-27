""" Listas y ciclos """
# Listas
estudiantes = ["Juan", "Pedro", "Maria", "Ana"]
lista_numerica = [1, 2, 3, 4, 5]
# Listas de listas
estudiantes_aula = [
    ["Juan", 20, "M"],
    ["Pedro", 22, "M"],
    ["Maria", 19, "F"],
    ["Ana", 21, "F"]
]
lista_vacia = []

print(estudiantes)
print(lista_numerica)
print(estudiantes[0])
print(estudiantes[1])  
print(estudiantes[2])
print(estudiantes[3])
print("------")
# for each
for estudiante in estudiantes:
    print(estudiante)
print("------")

#for i
for i in range(0,4):
    print(estudiantes[i])

print("------")

