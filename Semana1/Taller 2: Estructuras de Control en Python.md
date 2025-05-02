# 📘 Taller Evaluativo – Estructuras de Control en Python  
**(Versión Mejorada y Formal de los Enunciados)**

---

## ⭐ Nivel Básico

### ✅ 1. Cálculo de propina  
Desarrolle un programa que solicite al usuario dos números:  
- El costo total de una comida  
- El porcentaje de propina que desea dejar  

El programa debe calcular y mostrar el valor de la propina.

---

### ✅ 2. Comparación de dos números  
Cree un programa que solicite al usuario dos números enteros.  
Debe mostrar:  
- `"True"` si el primer número es mayor que el segundo  
- `"False"` en caso contrario  

⚠️ No debe incluir mensajes adicionales, solo el valor `"True"` o `"False"`.

---

### ✅ 3. Promedio de notas  
Implemente un programa que solicite las notas de tres parciales (números reales).  
Debe calcular el promedio y mostrar:  
- `"aprobado"` si el promedio es mayor o igual a 3.0  
- `"no aprobado"` si es menor  

⚠️ No debe imprimirse el promedio ni mensajes extra.

---

### ✅ 4. Clasificación de altura  
Cree un programa que solicite la altura del usuario en centímetros (entero).  
Clasifique según:  
- ≤ 150 cm: Altura baja  
- 151 – 170 cm: Altura media  
- > 170 cm: Altura alta  

---

### ✅ 5. Validación de clave de acceso  
Diseñe un programa que solicite al usuario ingresar una clave.  
Debe solicitarla de forma repetida hasta que escriba correctamente: `"python123"`.

---

### ✅ 6. División segura  
Solicite al usuario dos números enteros.  
- Si el segundo número es 0, debe pedirse nuevamente  
- Luego realice la división y muestre el resultado

---

## ⭐⭐ Nivel Intermedio

### ✅ 7. Cálculo de pérdidas por defectos  
Solicite la cantidad de puertas producidas (entero).  
Considere:  
- Por cada 1000 puertas, 14 son defectuosas  
- Cada puerta cuesta $180.000  

Calcule y muestre la **pérdida total** por defectos.

---

### ✅ 8. Clasificación de triángulos  
Solicite tres números enteros (lados de un triángulo).  
Determine si forman un triángulo válido. Si lo son, clasifique como:  
- Equilátero  
- Isósceles  
- Escaleno  

Si no forman un triángulo, mostrar: `"no se puede formar triangulo"`

---

### ✅ 9. Promoción de llantas  
Calcule el costo de una compra de llantas marca "Ponchadas":  
- < 5 llantas: $30.000 c/u  
- 5 a 10 llantas: $25.000 c/u  
- > 10 llantas: $20.000 c/u  

Debe mostrar:  
- Precio individual aplicado  
- Valor total de la compra

---

### ✅ 10. Descuento por compra de manzanas  
Determine el monto a pagar en una frutería con base en kilos comprados:  
- 0 – 2 kg: 0% descuento  
- > 2 – 5 kg: 10% descuento  
- > 5 – 10 kg: 15% descuento  
- > 10 kg: 20% descuento  

💰 Precio por kilo: $4.500

---

### ✅ 11. Promedio general de alumnos (while)  
Utilizando un ciclo `while`:  
- Solicite calificaciones de 10 alumnos (5 materias cada uno)  
- Calcule el promedio general del grupo  
- Muestre cuántos aprobaron (prom ≥ 7.0) y cuántos reprobaron

---

### ✅ 12. Promedio general de alumnos (for)  
Mismo requerimiento anterior, pero utilizando un ciclo `for`.

---

## ⭐⭐⭐ Nivel Avanzado

### 13. ✅ Diagnóstico de anemia  
Solicite al usuario:  
- Edad  
- Nivel de hemoglobina (g%)  

Con base en tablas médicas, determine si el resultado es:  
- `"positivo"` (anemia)  
- `"negativo"`

|         Edad         | Nivel normal de hemoglobina (g%) |
| ------------------ | ---- |
|       0 – 1 mes      |              13 – 26             |
|   >1 mes y ≤6 meses  |              10 – 18             |
| >6 meses y ≤12 meses |              11 – 15             |
|   >1 año y ≤5 años   |             11.5 – 15            |
|  >5 años y ≤10 años  |            12.6 – 15.5           |
|  >10 años y ≤15 años |             13 – 15.5            |

---

### ✅ 14. Factorial modificado  
Escriba un programa que solicite al usuario un **número entero positivo**.  
El programa debe calcular un **factorial modificado** según las siguientes reglas:

- Si el número ingresado es **par**, calcule el producto de **todos los números impares** desde 1 hasta llegar al número.
- Si el número ingresado es **impar**, calcule el producto de **todos los números pares** desde 2 hasta llegar al número.


#### ❓ ¿Qué es un factorial tradicional?
El factorial de un número `n`, denotado como `n!`, es el producto de todos los números enteros positivos desde 1 hasta `n`.

**Ejemplo clásico:** 5! = 5 × 4 × 3 × 2 × 1 = 120
⚠️ En este ejercicio **no** se debe calcular el factorial tradicional.  
Se deben **filtrar previamente** los números pares o impares según el caso.


### 📥 Entradas esperadas:
- Un número **entero positivo** (`int`)


### 🧪 Ejemplos esperados:

- Si el usuario ingresa `6`, el programa debe calcular `1 × 3 × 5 = 15`  
- Si el usuario ingresa `7`, el programa debe calcular `2 × 4 × 6 = 48`
