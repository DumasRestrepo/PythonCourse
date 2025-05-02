# 🧩 Tema: Listas y Diccionarios en Python

## 🎯 Objetivo del tema:

- Comprender qué son y cómo se utilizan las listas y los diccionarios.  
- Aprender a almacenar, acceder y modificar datos estructurados.  
- Aplicar operaciones básicas y recorridos con ciclos.  

---

## 1. ¿Qué es una lista?

Una lista es una colección **ordenada** y **mutable** de elementos, representada con corchetes `[]`.  
Puede contener cualquier tipo de dato: números, cadenas, booleanos, incluso otras listas.

**Ejemplos:**

`frutas = ["manzana", "banana", "cereza"]`  
`numeros = [10, 20, 30, 40]`

---

## 2. Operaciones comunes con listas

| Acción                | Ejemplo                         |
|-----------------------|----------------------------------|
| Acceder a un elemento | `frutas[0]` → `"manzana"`       |
| Modificar un valor    | `frutas[1] = "pera"`            |
| Agregar un elemento   | `frutas.append("kiwi")`         |
| Eliminar un elemento  | `frutas.remove("banana")`       |
| Tamaño de la lista    | `len(frutas)`                   |
| Ordenar la lista      | `numeros.sort()`                |
| Recorrer con `for`    | `for fruta in frutas: print(fruta)` |

---

## 3. Recorrer una lista con índices

`for i in range(len(frutas)):`  
  `print(f"Fruta {i}: {frutas[i]}")`

---

## 4. ¿Qué es un diccionario?

Un diccionario es una colección **no ordenada** de pares **clave:valor**, representado con llaves `{}`.  
Sirve para relacionar datos de forma más estructurada y descriptiva.

**Ejemplo:**

`estudiante = {`  
 `"nombre": "Laura",`  
 `"edad": 20,`  
 `"programa": "Ingeniería"`  
`}`

---

## 5. Acceso y modificación de valores

| Acción               | Ejemplo                                      |
|----------------------|-----------------------------------------------|
| Acceder a un valor   | `estudiante["nombre"]` → `"Laura"`           |
| Modificar un valor   | `estudiante["edad"] = 21`                    |
| Agregar nuevo par    | `estudiante["correo"] = "laura@mail.com"`   |
| Eliminar una clave   | `del estudiante["programa"]`                |
| Ver claves           | `estudiante.keys()`                          |
| Ver valores          | `estudiante.values()`                        |

---

## 6. Recorrer un diccionario

`for clave, valor in estudiante.items():`  
  `print(clave, ":", valor)`

📌 Esto imprime cada campo del diccionario junto con su valor.

---

## 7. Comparación rápida

| Característica     | Lista      | Diccionario     |
|--------------------|------------|-----------------|
| Ordenado           | ✅ Sí       | 🚫 No            |
| Acceso por         | Índice     | Clave           |
| Sintaxis           | `[]`       | `{}`            |
| Ideal para         | Datos en secuencia | Datos con nombre o etiquetas |

---

## 8. Uso combinado: lista de diccionarios

`agenda = [`  
 `{"nombre": "Ana", "tel": "123"},`  
 `{"nombre": "Luis", "tel": "456"}`  
`]`

`for contacto in agenda:`  
  `print(contacto["nombre"], "->", contacto["tel"])`

Esto permite representar estructuras complejas, como registros, bases de datos simples, etc.

---

## 🧠 Tip Final

- Las **listas** almacenan **valores secuenciales**.  
- Los **diccionarios** almacenan **datos con significado**.  
Usar bien estas estructuras permite construir programas eficientes, organizados y potentes.

---

## ✅ Actividades sugeridas

- Crear una lista con los nombres de 5 estudiantes y recorrerla para saludarlos.  
- Crear un diccionario que represente los datos personales de un usuario.  
- Crear una lista de diccionarios para representar una tabla de notas.  
- Escribir una función que reciba una lista de números y devuelva un diccionario con el número mayor, menor y promedio.
