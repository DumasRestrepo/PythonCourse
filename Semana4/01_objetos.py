class person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def despedirse(self,nombre):
        print(f"Adiós, soy {self.nombre} y tengo {self.edad} años.")

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    
    def agregar_nota(self, nota):# Setea una nota
        self.notas.append(nota)
        print(f"Nota {nota} agregada a {self.nombre}.")

    def mostrar_notas(self): #getter
        # Muestra las notas del estudiante
        if self.notas != []:
            print(f"Notas de {self.nombre}: {', '.join(map(str, self.notas))}")
        else:
            print(f"{self.nombre} no tiene notas.")

class estudiante(person):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def mostrar_carrera(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")

if __name__ == "__main__":
    # Definición de la clase 
    persona1 = person("Juan", 30)
    persona1.saludar()
    persona2 = person("María", 25)
    persona2.saludar()

    persona2.agregar_nota(5)
    persona2.mostrar_notas()
    persona1.mostrar_notas()
    persona3  =estudiante("Pedro", 20, "Ingeniería")
    persona3.saludar()
    persona3.mostrar_carrera()
    persona3.agregar_nota(8)
    persona3.mostrar_notas()
