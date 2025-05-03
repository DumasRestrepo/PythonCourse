# 🧩 Tema: Funciones y Reutilización de Código



## 1. ¿Qué es una función?

Una función es un bloque de código que realiza una tarea específica y puede ejecutarse en cualquier momento del programa con solo llamarla por su nombre.

👉 Es como una herramienta que creas una vez y puedes usar muchas veces.

---

## 2. ¿Por qué usar funciones?

Usar funciones nos permite:

✅ Evitar repetir código innecesariamente  
✅ Organizar mejor nuestros programas en pequeñas piezas lógicas  
✅ Facilitar el mantenimiento: puedes corregir errores en un solo lugar  
✅ Mejorar la legibilidad del código  
✅ Reutilizar el código en otros proyectos o partes del mismo programa  

---

## 3. Estructura de una función

Ejemplo general:

`def nombre_de_la_funcion(parámetros):`  
 `# Cuerpo o bloque de instrucciones`  
 `return valor_opcional`

Ejemplo básico:

`def saludar():`  
 `print("Hola, bienvenido al curso")`

Para ejecutarla (llamarla):  
`saludar()`

📌 Importante: El código dentro de la función no se ejecuta automáticamente, solo cuando la llamamos.

---

## 4. Parámetros y argumentos

Una función puede recibir parámetros (valores que necesita para trabajar).

`def saludar_persona(nombre):`  
 `print(f"Hola, {nombre}")`

Al llamarla:  
`saludar_persona("Christian")`

---

## 5. Retorno de valores (`return`)

Una función puede devolver un resultado con la palabra clave `return`:

`def sumar(a, b):`  
 `return a + b`  

`resultado = sumar(4, 5)`  
`print("La suma es:", resultado)`

📌 `return` devuelve un valor al lugar donde se llamó la función.  
Sin `return`, la función solo ejecuta acciones pero no entrega resultados.

---

## 6. Funciones que procesan listas

`def obtener_promedio(lista_notas):`  
 `return sum(lista_notas) / len(lista_notas)`

`notas = [3.5, 4.2, 5.0]`  
`print("Promedio:", obtener_promedio(notas))`

---

## 7. Reutilización de funciones

Una vez definida, una función puede usarse en cualquier parte del programa, tantas veces como se necesite:

`def cuadrado(x):`  
 `return x * x`

`print(cuadrado(2))`  
`print(cuadrado(5))`  
`print(cuadrado(10))`

Esto permite construir programas más grandes sin repetir bloques de código.

---

## 8. Composición de funciones (una función llama a otra)

`def obtener_promedio(notas):`  
 `return sum(notas) / len(notas)`

`def estado_academico(notas):`  
 `promedio = obtener_promedio(notas)`  
 `if promedio >= 3.0:`  
  `return "Aprobado"`  
 `else:`  
  `return "Reprobado"`

---

## 9. Buenas prácticas al usar funciones

- Usa nombres descriptivos (evita nombres como `f1`, `f2`).  
- No pongas demasiadas tareas en una sola función.  
- Comenta funciones complejas.  
- Reutiliza funciones existentes antes de escribir nuevas.  
- Si una tarea se repite más de una vez → conviértela en función.
